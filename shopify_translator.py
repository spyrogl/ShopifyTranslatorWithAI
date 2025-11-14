#!/usr/bin/env python3
"""
Shopify Product Translator with OpenAI
Translate Shopify product exports to multiple languages with market adaptation.
"""

import os
import sys
import json
import time
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import pandas as pd
from openai import OpenAI
from colorama import init, Fore, Back, Style
from tqdm import tqdm

# Import language definitions
from languages import ALL_LANGUAGES, get_translation_prompt, STANDARD_OPTION_NAMES_EXTENDED

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# Constants
CONFIG_FILE = "config.json"
CACHE_FILE = "translation_cache.json"
BACKUP_DIR = "backups"
OUTPUT_DIR = "translated_outputs"

# Standard sizes that should not be translated
STANDARD_SIZES = ['XS', 'S', 'M', 'L', 'XL', 'XXL', '2XL', '3XL', '4XL', '5XL']



# Fields that can be translated
TRANSLATABLE_FIELDS = [
    'Title',
    'Body (HTML)',
    'Type',
    'Tags',
    'Option1 Name',
    'Option1 Value',
    'Option2 Name',
    'Option2 Value',
    'Option3 Name',
    'Option3 Value',
    'Image Alt Text',
    'SEO Title',
    'SEO Description'
]

# Use comprehensive language list from languages module
MARKET_ADAPTATIONS = ALL_LANGUAGES

# Update STANDARD_OPTION_NAMES to use extended version
STANDARD_OPTION_NAMES = STANDARD_OPTION_NAMES_EXTENDED


class ShopifyTranslator:
    def __init__(self):
        self.client = None
        self.config = {}
        self.cache = {}
        self.df = None
        self.backup_path = None
        self.total_cost = 0.0
        self.total_tokens = 0

    def print_header(self, text: str):
        """Print styled header"""
        print(f"\n{Fore.CYAN}{Style.BRIGHT}{'='*60}")
        print(f"{text.center(60)}")
        print(f"{'='*60}{Style.RESET_ALL}\n")

    def print_success(self, text: str):
        """Print success message"""
        print(f"{Fore.GREEN}✓ {text}{Style.RESET_ALL}")

    def print_error(self, text: str):
        """Print error message"""
        print(f"{Fore.RED}✗ {text}{Style.RESET_ALL}")

    def print_warning(self, text: str):
        """Print warning message"""
        print(f"{Fore.YELLOW}⚠ {text}{Style.RESET_ALL}")

    def print_info(self, text: str):
        """Print info message"""
        print(f"{Fore.BLUE}ℹ {text}{Style.RESET_ALL}")

    def load_config(self) -> Dict:
        """Load configuration from file"""
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_config(self, config: Dict):
        """Save configuration to file"""
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        self.print_success(f"Configuration saved to {CONFIG_FILE}")

    def load_cache(self) -> Dict:
        """Load translation cache"""
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_cache(self):
        """Save translation cache"""
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, indent=2, ensure_ascii=False)

    def setup_api_key(self):
        """Step 1: Configure OpenAI API key"""
        self.print_header("Step 1: API Configuration")

        self.config = self.load_config()

        if 'openai_api_key' in self.config:
            self.print_info(f"Found existing API key: {self.config['openai_api_key'][:8]}...")
            use_existing = input(f"{Fore.YELLOW}Use existing key? (yes/no): {Style.RESET_ALL}").strip().lower()
            if use_existing == 'yes':
                api_key = self.config['openai_api_key']
            else:
                api_key = input(f"{Fore.YELLOW}Enter your OpenAI API key: {Style.RESET_ALL}").strip()
        else:
            print("You need an OpenAI API key to use this translator.")
            print(f"{Fore.CYAN}Get one here: https://platform.openai.com/api-keys{Style.RESET_ALL}\n")
            api_key = input(f"{Fore.YELLOW}Enter your OpenAI API key: {Style.RESET_ALL}").strip()

        # Validate API key
        try:
            self.client = OpenAI(api_key=api_key)
            # Test with a minimal request
            self.client.models.list()
            self.print_success("API key validated successfully!")

            # Save to config
            self.config['openai_api_key'] = api_key
            self.save_config(self.config)

        except Exception as e:
            self.print_error(f"API key validation failed: {str(e)}")
            self.print_info("Please check your API key at https://platform.openai.com/api-keys")
            sys.exit(1)

    def load_csv_file(self):
        """Step 2: Load CSV file with backup"""
        self.print_header("Step 2: Load CSV File")

        # Get file path
        if len(sys.argv) > 1:
            csv_path = sys.argv[1]
        else:
            csv_path = input(f"{Fore.YELLOW}Enter path to Shopify CSV file: {Style.RESET_ALL}").strip()
            # Remove quotes if user dragged and dropped
            csv_path = csv_path.strip('"').strip("'")

        if not os.path.exists(csv_path):
            self.print_error(f"File not found: {csv_path}")
            sys.exit(1)

        # Create backup
        os.makedirs(BACKUP_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.basename(csv_path)
        self.backup_path = os.path.join(BACKUP_DIR, f"backup_{timestamp}_{filename}")

        try:
            # Load CSV
            self.df = pd.read_csv(csv_path, encoding='utf-8')

            # Create backup
            self.df.to_csv(self.backup_path, index=False, encoding='utf-8')

            self.print_success(f"File loaded: {len(self.df)} rows")
            self.print_success(f"Backup created: {self.backup_path}")

        except Exception as e:
            self.print_error(f"Could not read CSV file: {str(e)}")
            self.print_info("Make sure it's a valid Shopify export in UTF-8 encoding")
            sys.exit(1)

    def analyze_file(self) -> Dict:
        """Step 3: Analyze CSV structure"""
        self.print_header("Step 3: File Analysis")

        # Count unique products (by Handle)
        unique_products = self.df['Handle'].nunique()
        total_rows = len(self.df)

        # Detect translatable fields
        available_fields = [f for f in TRANSLATABLE_FIELDS if f in self.df.columns]

        analysis = {
            'unique_products': unique_products,
            'total_rows': total_rows,
            'available_fields': available_fields
        }

        print(f"{Fore.GREEN}Products found: {unique_products}")
        print(f"Total variants/rows: {total_rows}")
        print(f"Average variants per product: {total_rows / unique_products:.1f}{Style.RESET_ALL}\n")

        # Show first product preview
        first_handle = self.df['Handle'].iloc[0]
        first_product = self.df[self.df['Handle'] == first_handle]

        print(f"{Fore.CYAN}Preview of first product:{Style.RESET_ALL}")
        print(f"  Handle: {first_handle}")
        if 'Title' in self.df.columns and pd.notna(first_product['Title'].iloc[0]):
            print(f"  Title: {first_product['Title'].iloc[0][:60]}...")
        if 'Type' in self.df.columns and pd.notna(first_product['Type'].iloc[0]):
            print(f"  Type: {first_product['Type'].iloc[0]}")
        print(f"  Variants: {len(first_product)}")

        return analysis

    def select_fields(self, available_fields: List[str]) -> List[str]:
        """Step 4: Field selection"""
        self.print_header("Step 4: Field Selection")

        print(f"{Fore.CYAN}Available fields for translation:{Style.RESET_ALL}\n")
        for i, field in enumerate(available_fields, 1):
            print(f"  {i}. {field}")

        print(f"\n{Fore.YELLOW}Selection options:")
        print("  - Enter numbers separated by commas (e.g., 1,2,5)")
        print("  - Enter 'all' for all fields")
        print("  - Enter 'basic' for Title and Body only")
        print(f"  - Press Enter for recommended: Title, Body, Type, Option Names & Values{Style.RESET_ALL}\n")

        selection = input(f"{Fore.YELLOW}Select fields: {Style.RESET_ALL}").strip().lower()

        if selection == 'all':
            selected = available_fields
        elif selection == 'basic':
            selected = [f for f in ['Title', 'Body (HTML)'] if f in available_fields]
        elif selection == '':
            # Recommended fields
            selected = [f for f in ['Title', 'Body (HTML)', 'Type', 'Option1 Name', 'Option1 Value', 'Option2 Name', 'Option2 Value'] if f in available_fields]
        else:
            try:
                indices = [int(x.strip()) - 1 for x in selection.split(',')]
                selected = [available_fields[i] for i in indices if 0 <= i < len(available_fields)]
            except:
                self.print_error("Invalid selection, using recommended fields")
                selected = [f for f in ['Title', 'Body (HTML)', 'Type', 'Option1 Name', 'Option1 Value', 'Option2 Name', 'Option2 Value'] if f in available_fields]

        self.print_success(f"Selected {len(selected)} fields: {', '.join(selected)}")
        return selected

    def get_translation_settings(self) -> Dict:
        """Step 5: Translation settings"""
        self.print_header("Step 5: Translation Settings")

        # Target language
        print(f"{Fore.CYAN}Available languages:{Style.RESET_ALL}\n")
        languages = list(MARKET_ADAPTATIONS.keys())
        for i, lang_key in enumerate(languages, 1):
            lang = MARKET_ADAPTATIONS[lang_key]
            print(f"  {i}. {lang['name']}")

        default_lang = self.config.get('default_language', 'greek')
        print(f"\n{Fore.YELLOW}Default: {default_lang}{Style.RESET_ALL}")

        lang_input = input(f"{Fore.YELLOW}Select language (name or number, or press Enter for {default_lang}): {Style.RESET_ALL}").strip().lower()

        if lang_input == '':
            target_language = default_lang
        elif lang_input.isdigit() and 1 <= int(lang_input) <= len(languages):
            target_language = languages[int(lang_input) - 1]
        elif lang_input in languages:
            target_language = lang_input
        else:
            self.print_warning(f"Invalid selection, using {default_lang}")
            target_language = default_lang

        # Translation mode
        print(f"\n{Fore.CYAN}Translation modes:{Style.RESET_ALL}\n")
        print(f"  1. Direct Translation - Literal, word-for-word (fast, accurate)")
        print(f"  2. Market Adaptation - Localized, natural phrasing {Fore.GREEN}(recommended){Style.RESET_ALL}")

        mode_input = input(f"\n{Fore.YELLOW}Select mode (1 or 2, or press Enter for Market Adaptation): {Style.RESET_ALL}").strip()

        if mode_input == '1':
            translation_mode = 'direct'
        else:
            translation_mode = 'market_adaptation'

        # Model selection
        print(f"\n{Fore.CYAN}OpenAI models:{Style.RESET_ALL}\n")
        print(f"  1. GPT-4o-mini {Fore.GREEN}(recommended){Style.RESET_ALL} - Fast, excellent quality, ~$0.001/product")
        print(f"  2. GPT-4o (premium) - Outstanding quality, ~$0.013/product")

        model_input = input(f"\n{Fore.YELLOW}Select model (1 or 2, or press Enter for GPT-4o-mini): {Style.RESET_ALL}").strip()

        if model_input == '2':
            model = 'gpt-4o'
        else:
            model = 'gpt-4o-mini'

        # Special instructions
        print(f"\n{Fore.CYAN}Special instructions (optional):{Style.RESET_ALL}")
        print("  Examples:")
        print("  - 'Winter clothing emphasizing warmth and style'")
        print("  - 'Luxury items with sophisticated language'")
        print("  - 'Men's fashion for ages 25-50'")

        special_instructions = input(f"\n{Fore.YELLOW}Enter special instructions (or press Enter to skip): {Style.RESET_ALL}").strip()

        # Shoe size conversion
        print(f"\n{Fore.CYAN}Shoe size conversion (optional):{Style.RESET_ALL}")
        print("  1. None - Keep sizes as they are")
        print("  2. US → EU - Convert US sizes to European sizes")
        print("  3. EU → US - Convert European sizes to US sizes")

        shoe_input = input(f"\n{Fore.YELLOW}Select conversion (1-3, or press Enter for None): {Style.RESET_ALL}").strip()

        if shoe_input == '2':
            shoe_conversion = 'us_to_eu'
        elif shoe_input == '3':
            shoe_conversion = 'eu_to_us'
        else:
            shoe_conversion = 'none'

        settings = {
            'target_language': target_language,
            'translation_mode': translation_mode,
            'model': model,
            'special_instructions': special_instructions,
            'shoe_conversion': shoe_conversion
        }

        # Save as defaults
        self.config['default_language'] = target_language
        self.config['default_mode'] = translation_mode
        self.config['default_model'] = model
        self.save_config(self.config)

        return settings

    def estimate_cost(self, selected_fields: List[str], settings: Dict) -> Dict:
        """Step 6: Estimate translation cost"""
        self.print_header("Step 6: Cost Estimate")

        unique_products = self.df['Handle'].nunique()

        # Estimate tokens per product
        sample_text_length = 0
        for field in selected_fields:
            if field in self.df.columns:
                # Get first non-null value for estimation
                sample = self.df[field].dropna().iloc[0] if len(self.df[field].dropna()) > 0 else ""
                sample_text_length += len(str(sample))

        # Rough token estimation (1 token ≈ 4 characters)
        estimated_tokens_per_product = sample_text_length // 4
        total_tokens = estimated_tokens_per_product * unique_products

        # Cost per token (pricing as of 2024)
        if settings['model'] == 'gpt-4o-mini':
            cost_per_1k_tokens = 0.00015  # Input tokens
            cost_per_product = 0.001
        else:  # gpt-4o
            cost_per_1k_tokens = 0.0025  # Input tokens
            cost_per_product = 0.013

        estimated_cost_min = total_tokens / 1000 * cost_per_1k_tokens
        estimated_cost_max = estimated_cost_min * 2  # Account for output tokens

        # Estimated time (rough estimate: 2-3 seconds per product)
        estimated_time_min = unique_products * 2
        estimated_time_max = unique_products * 3

        estimate = {
            'products': unique_products,
            'fields': len(selected_fields),
            'tokens': total_tokens,
            'cost_min': estimated_cost_min,
            'cost_max': estimated_cost_max,
            'time_min': estimated_time_min,
            'time_max': estimated_time_max
        }

        # Display estimate
        print(f"{Fore.CYAN}{'─'*50}")
        print(f"  Products to translate: {Fore.GREEN}{unique_products}")
        print(f"{Fore.CYAN}  Fields selected: {Fore.GREEN}{len(selected_fields)} ({', '.join(selected_fields[:3])}{'...' if len(selected_fields) > 3 else ''})")
        print(f"{Fore.CYAN}  Target language: {Fore.GREEN}{MARKET_ADAPTATIONS[settings['target_language']]['name']}")
        print(f"{Fore.CYAN}  Model: {Fore.GREEN}{settings['model']}")
        print(f"{Fore.CYAN}  {'─'*50}")
        print(f"  Estimated tokens: {Fore.YELLOW}~{total_tokens:,}")
        print(f"{Fore.CYAN}  Estimated cost: {Fore.YELLOW}${estimated_cost_min:.3f} - ${estimated_cost_max:.3f} USD")
        print(f"{Fore.CYAN}  Estimated time: {Fore.YELLOW}{estimated_time_min//60}-{estimated_time_max//60} minutes")
        print(f"{Fore.CYAN}{'─'*50}{Style.RESET_ALL}\n")

        proceed = input(f"{Fore.YELLOW}Proceed with translation? (yes/no): {Style.RESET_ALL}").strip().lower()

        if proceed != 'yes':
            self.print_info("Translation cancelled")
            sys.exit(0)

        return estimate

    def create_cache_key(self, text: str, target_lang: str, mode: str) -> str:
        """Create cache key for translation"""
        return f"{text}||{target_lang}||{mode}"

    def remove_personal_names(self, text: str, field_name: str = "") -> str:
        """Remove personal names from titles and descriptions for professional branding"""
        if field_name not in ['Title', 'Body (HTML)']:
            return text

        # Common patterns where names appear in product titles
        patterns = [
            r'\s*\|\s*[A-Z][a-z]+\s*$',  # | Charles at end
            r'\s*-\s*[A-Z][a-z]+\s*$',   # - Charles at end
            r'\s*by\s+[A-Z][a-z]+\s*$',  # by Charles at end
            r'\s*\|\s*[A-Z][a-z]+\s+[A-Z][a-z]+\s*$',  # | John Smith at end
            r'\s*-\s*[A-Z][a-z]+\s+[A-Z][a-z]+\s*$',   # - John Smith at end
            r'\s*by\s+[A-Z][a-z]+\s+[A-Z][a-z]+\s*$',  # by John Smith at end
        ]

        cleaned_text = text
        for pattern in patterns:
            cleaned_text = re.sub(pattern, '', cleaned_text, flags=re.IGNORECASE)

        # Remove any trailing pipes or dashes left over
        cleaned_text = re.sub(r'\s*[\|\-]\s*$', '', cleaned_text)

        return cleaned_text.strip()

    def translate_text(self, text: str, settings: Dict, field_name: str = "") -> str:
        """Translate text using OpenAI API with caching"""
        if pd.isna(text) or text == "":
            return text

        # Remove personal names from titles and descriptions
        text = self.remove_personal_names(str(text), field_name)

        # Check for standard Option Names (Color, Size, etc.) for consistent branding
        if field_name in ['Option1 Name', 'Option2 Name', 'Option3 Name']:
            target_lang = settings['target_language']
            text_lower = str(text).lower().strip()

            if target_lang in STANDARD_OPTION_NAMES:
                if text_lower in STANDARD_OPTION_NAMES[target_lang]:
                    standard_translation = STANDARD_OPTION_NAMES[target_lang][text_lower]
                    # Cache this for consistency
                    cache_key = self.create_cache_key(str(text), target_lang, settings['translation_mode'])
                    self.cache[cache_key] = standard_translation
                    return standard_translation

        # Check cache
        cache_key = self.create_cache_key(str(text), settings['target_language'], settings['translation_mode'])
        if cache_key in self.cache:
            return self.cache[cache_key]

        # Skip translation for standard sizes
        if field_name in ['Option2 Value', 'Option3 Value'] and str(text).upper() in STANDARD_SIZES:
            return text

        # Build prompt
        lang_info = MARKET_ADAPTATIONS[settings['target_language']]

        # Get generic translation prompt without location references
        base_prompt = get_translation_prompt(
            lang_info['name'],
            lang_info['code'],
            settings['translation_mode']
        )

        if settings['translation_mode'] == 'market_adaptation':
            # Special formatting for product descriptions (Body HTML)
            if field_name == 'Body (HTML)':
                system_prompt = f"""{base_prompt}

{"Special context: " + settings['special_instructions'] if settings['special_instructions'] else ""}

CRITICAL FORMATTING REQUIREMENTS:
- Structure the translation with:
  1. One short introductory paragraph (2-3 sentences maximum)
  2. Followed by EXACTLY 4 bullet points (no more, no less)
- Use HTML tags: <p> for paragraph, <ul> and <li> for bullet points
- Format example:
  <p>Short description here.</p>
  <ul>
  <li>First key feature</li>
  <li>Second key feature</li>
  <li>Third key feature</li>
  <li>Fourth key feature</li>
  </ul>

IMPORTANT:
- DO NOT mention any specific countries, cities, regions, or locations
- Focus only on product features and benefits
- Preserve ALL HTML tags exactly
- MUST have exactly 4 bullet points
- Keep description concise and compelling
- Return ONLY the translated HTML, no explanations"""
            else:
                system_prompt = f"""{base_prompt}

{"Special context: " + settings['special_instructions'] if settings['special_instructions'] else ""}

IMPORTANT:
- DO NOT mention any specific countries, cities, regions, or locations
- Focus only on product features and benefits
- If the text contains HTML tags, preserve ALL HTML tags exactly as they are
- Keep the same structure and formatting
- Only translate the actual text content, not HTML tags or attributes
- Return ONLY the translated text, no explanations"""
        else:
            system_prompt = f"""{base_prompt}

IMPORTANT:
- DO NOT mention any specific countries, cities, regions, or locations
- If the text contains HTML tags, preserve ALL HTML tags exactly as they are
- Return ONLY the translated text, no explanations"""

        try:
            response = self.client.chat.completions.create(
                model=settings['model'],
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": text}
                ],
                temperature=0.3 if settings['translation_mode'] == 'direct' else 0.7
            )

            translated = response.choices[0].message.content.strip()

            # Update cost tracking
            self.total_tokens += response.usage.total_tokens

            # Cache the translation
            self.cache[cache_key] = translated

            # Small delay to respect rate limits
            time.sleep(0.5)

            return translated

        except Exception as e:
            self.print_warning(f"Translation failed for text (keeping original): {str(e)[:50]}")
            return text

    def translate_products(self, selected_fields: List[str], settings: Dict):
        """Step 7: Translate products with progress tracking"""
        self.print_header("Step 7: Translation Process")

        # Load existing cache
        self.cache = self.load_cache()

        # Get unique products
        unique_handles = self.df['Handle'].unique()

        # Progress bar
        pbar = tqdm(
            total=len(unique_handles),
            desc="Translating products",
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]",
            colour='green'
        )

        start_time = time.time()

        for handle in unique_handles:
            # Get all rows for this product
            product_rows = self.df[self.df['Handle'] == handle]
            first_row_idx = product_rows.index[0]

            # Show current product
            title = self.df.at[first_row_idx, 'Title'] if 'Title' in self.df.columns and pd.notna(self.df.at[first_row_idx, 'Title']) else handle
            pbar.set_postfix_str(f"{title[:40]}...")

            # Translate main product info (first row only)
            for field in selected_fields:
                if field not in self.df.columns:
                    continue

                # Special handling for Option Names and Values (variants)
                if field in ['Option1 Name', 'Option2 Name', 'Option3 Name',
                             'Option1 Value', 'Option2 Value', 'Option3 Value']:
                    # Get all unique values for this field across all variants
                    unique_values = product_rows[field].dropna().unique()

                    # Translate each unique value once and apply to all matching rows
                    for unique_val in unique_values:
                        if unique_val and str(unique_val).strip():
                            translated_val = self.translate_text(str(unique_val), settings, field)
                            # Apply translation to ALL rows with this value
                            mask = (self.df['Handle'] == handle) & (self.df[field] == unique_val)
                            self.df.loc[mask, field] = translated_val
                else:
                    # For non-variant fields, translate only the first row
                    value = self.df.at[first_row_idx, field]
                    if pd.notna(value) and value != "":
                        translated = self.translate_text(str(value), settings, field)
                        self.df.at[first_row_idx, field] = translated

            pbar.update(1)

            # Save cache periodically (every 10 products)
            if len([h for h in unique_handles if h == handle]) % 10 == 0:
                self.save_cache()

        pbar.close()

        # Save final cache
        self.save_cache()

        # Apply shoe size conversion if requested
        if settings.get('shoe_conversion', 'none') != 'none':
            print(f"\n{Fore.CYAN}Converting shoe sizes...{Style.RESET_ALL}")
            from shoe_size_converter import ShoeSizeConverter

            # Fields that might contain shoe sizes
            size_fields = ['Option1 Value', 'Option2 Value', 'Option3 Value', 'Variant Size', 'Title']

            for idx, row in self.df.iterrows():
                # Get context for gender detection (title, type, etc.)
                context = ""
                if 'Title' in self.df.columns:
                    context += str(row.get('Title', '')) + " "
                if 'Type' in self.df.columns:
                    context += str(row.get('Type', '')) + " "
                if 'Body (HTML)' in self.df.columns:
                    context += str(row.get('Body (HTML)', ''))[:200]  # First 200 chars

                # Convert sizes in each field
                for field in size_fields:
                    if field in self.df.columns:
                        value = row.get(field)
                        if pd.notna(value) and value != "":
                            # Convert based on direction
                            if settings['shoe_conversion'] == 'us_to_eu':
                                converted = ShoeSizeConverter.convert_size_in_text(
                                    str(value), 'us_to_eu', context
                                )
                            elif settings['shoe_conversion'] == 'eu_to_us':
                                converted = ShoeSizeConverter.convert_size_in_text(
                                    str(value), 'eu_to_us', context
                                )
                            else:
                                converted = value

                            self.df.at[idx, field] = converted

            self.print_success("Shoe size conversion completed")

        elapsed_time = time.time() - start_time

        # Calculate actual cost
        if settings['model'] == 'gpt-4o-mini':
            cost_per_1k = 0.00015
        else:
            cost_per_1k = 0.0025

        self.total_cost = (self.total_tokens / 1000) * cost_per_1k * 2  # Multiply by 2 for output tokens

        self.print_success(f"\nTranslation completed in {elapsed_time/60:.1f} minutes")
        self.print_info(f"Total tokens used: {self.total_tokens:,}")
        self.print_info(f"Actual cost: ${self.total_cost:.3f} USD")

    def save_output(self, settings: Dict):
        """Step 8: Save translated CSV"""
        self.print_header("Step 8: Save Results")

        # Create output directory
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Generate output filename
        timestamp = datetime.now().strftime("%Y%m%d")
        lang_name = settings['target_language']
        original_name = os.path.basename(self.backup_path).replace('backup_', '').replace('.csv', '')

        output_filename = f"{original_name}_{lang_name}_{timestamp}.csv"
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        # Save CSV
        try:
            self.df.to_csv(output_path, index=False, encoding='utf-8')
            self.print_success(f"Output saved: {output_path}")

            # Validation
            original_rows = len(self.df)
            saved_df = pd.read_csv(output_path, encoding='utf-8')
            saved_rows = len(saved_df)

            if original_rows == saved_rows:
                self.print_success(f"Validation passed: {saved_rows} rows preserved")
            else:
                self.print_warning(f"Row count mismatch: {original_rows} -> {saved_rows}")

            # Summary
            print(f"\n{Fore.CYAN}{'='*60}")
            print(f"{Fore.GREEN}{Style.BRIGHT}✓ Translation Complete!{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'='*60}")
            print(f"\n{Fore.CYAN}Output file: {Fore.GREEN}{output_path}")
            print(f"{Fore.CYAN}Total tokens: {Fore.GREEN}{self.total_tokens:,}")
            print(f"{Fore.CYAN}Total cost: {Fore.GREEN}${self.total_cost:.3f} USD")
            print(f"\n{Fore.GREEN}{Style.BRIGHT}Ready to import to Shopify!{Style.RESET_ALL}\n")

        except Exception as e:
            self.print_error(f"Failed to save output: {str(e)}")
            sys.exit(1)

    def run(self):
        """Main workflow"""
        try:
            # ASCII Art Header
            print(f"\n{Fore.CYAN}{Style.BRIGHT}")
            print("╔═══════════════════════════════════════════════════════════╗")
            print("║                                                           ║")
            print("║          SHOPIFY PRODUCT TRANSLATOR WITH AI              ║")
            print("║         Powered by OpenAI for Market Adaptation          ║")
            print("║                                                           ║")
            print("╚═══════════════════════════════════════════════════════════╝")
            print(f"{Style.RESET_ALL}\n")

            # Run workflow
            self.setup_api_key()
            self.load_csv_file()
            analysis = self.analyze_file()
            selected_fields = self.select_fields(analysis['available_fields'])
            settings = self.get_translation_settings()
            self.estimate_cost(selected_fields, settings)
            self.translate_products(selected_fields, settings)
            self.save_output(settings)

        except KeyboardInterrupt:
            self.print_warning("\n\nTranslation interrupted by user")
            self.print_info("Progress has been saved to cache")
            sys.exit(0)
        except Exception as e:
            self.print_error(f"Unexpected error: {str(e)}")
            import traceback
            traceback.print_exc()
            sys.exit(1)


def main():
    translator = ShopifyTranslator()
    translator.run()


if __name__ == "__main__":
    main()
