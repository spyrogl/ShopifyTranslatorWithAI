#!/usr/bin/env python3
"""
Demo Script for Shopify Translator
Preview translations without using API credits
"""

import os
import pandas as pd
from colorama import init, Fore, Style

init(autoreset=True)

# Mock translations for demonstration
MOCK_TRANSLATIONS = {
    'greek': {
        'Elegant winter coat for men | Charles': 'Κομψό χειμερινό παλτό για άνδρες | Charles',
        'Jackets': 'Μπουφάν',
        'Blue': 'Μπλε',
        'Black': 'Μαύρο',
        'Green': 'Πράσινο',
        'Stay warm and stylish this winter with our elegant winter coat':
            'Μείνετε ζεστοί και κομψοί αυτόν τον χειμώνα με το κομψό μας χειμερινό παλτό',
    },
    'dutch': {
        'Elegant winter coat for men | Charles': 'Elegante winterjas voor mannen | Charles',
        'Jackets': 'Jassen',
        'Blue': 'Blauw',
        'Black': 'Zwart',
        'Green': 'Groen',
        'Stay warm and stylish this winter with our elegant winter coat':
            'Blijf warm en stijlvol deze winter met onze elegante winterjas',
    },
    'german': {
        'Elegant winter coat for men | Charles': 'Eleganter Wintermantel für Männer | Charles',
        'Jackets': 'Jacken',
        'Blue': 'Blau',
        'Black': 'Schwarz',
        'Green': 'Grün',
        'Stay warm and stylish this winter with our elegant winter coat':
            'Bleiben Sie warm und stilvoll diesen Winter mit unserem eleganten Wintermantel',
    }
}


def print_header(text):
    print(f"\n{Fore.CYAN}{Style.BRIGHT}{'='*60}")
    print(f"{text.center(60)}")
    print(f"{'='*60}{Style.RESET_ALL}\n")


def mock_translate(text, language):
    """Mock translation function"""
    if language in MOCK_TRANSLATIONS and text in MOCK_TRANSLATIONS[language]:
        return MOCK_TRANSLATIONS[language][text]
    return f"[{language.upper()}] {text}"


def demo_translation():
    """Run a demo translation"""
    print_header("SHOPIFY TRANSLATOR - DEMO MODE")

    print(f"{Fore.YELLOW}This demo shows how translations would work WITHOUT using API credits.{Style.RESET_ALL}\n")

    # Sample product data
    print(f"{Fore.CYAN}Sample Product:{Style.RESET_ALL}")
    print("  Handle: elegant-winter-coat-for-men-charles")
    print("  Title: Elegant winter coat for men | Charles")
    print("  Type: Jackets")
    print("  Color: Blue")
    print("  Description: Stay warm and stylish this winter with our elegant winter coat\n")

    # Show translations
    languages = ['greek', 'dutch', 'german']

    for lang in languages:
        lang_names = {
            'greek': 'Greek (Ελληνικά)',
            'dutch': 'Dutch (Nederlands)',
            'german': 'German (Deutsch)'
        }

        print(f"\n{Fore.GREEN}{'─'*60}")
        print(f"Translation to {lang_names[lang]}:")
        print(f"{'─'*60}{Style.RESET_ALL}")

        print(f"{Fore.CYAN}Title:{Style.RESET_ALL}")
        print(f"  Original: Elegant winter coat for men | Charles")
        print(f"  Translated: {mock_translate('Elegant winter coat for men | Charles', lang)}\n")

        print(f"{Fore.CYAN}Type:{Style.RESET_ALL}")
        print(f"  Original: Jackets")
        print(f"  Translated: {mock_translate('Jackets', lang)}\n")

        print(f"{Fore.CYAN}Color:{Style.RESET_ALL}")
        print(f"  Original: Blue")
        print(f"  Translated: {mock_translate('Blue', lang)}\n")

        print(f"{Fore.CYAN}Description:{Style.RESET_ALL}")
        desc = 'Stay warm and stylish this winter with our elegant winter coat'
        print(f"  Original: {desc}")
        print(f"  Translated: {mock_translate(desc, lang)}\n")

    # Cost estimate
    print(f"\n{Fore.YELLOW}{'═'*60}")
    print("ESTIMATED COSTS (with real API):")
    print(f"{'═'*60}{Style.RESET_ALL}")
    print(f"\n{Fore.CYAN}For 1 product with Title, Description, Type, and Colors:")
    print(f"  Model: GPT-4o-mini")
    print(f"  Estimated tokens: ~500")
    print(f"  Estimated cost: $0.001 USD{Style.RESET_ALL}")

    print(f"\n{Fore.CYAN}For 50 products:")
    print(f"  Estimated cost: $0.03 - $0.05 USD{Style.RESET_ALL}")

    print(f"\n{Fore.CYAN}For 100 products:")
    print(f"  Estimated cost: $0.10 - $0.50 USD{Style.RESET_ALL}")

    print(f"\n{Fore.GREEN}{'═'*60}")
    print("DEMO COMPLETE!")
    print(f"{'═'*60}{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}To run real translations:")
    print(f"  1. Get an OpenAI API key from https://platform.openai.com/api-keys")
    print(f"  2. Run: python shopify_translator.py products_export.csv")
    print(f"  3. Follow the interactive prompts{Style.RESET_ALL}\n")


def analyze_sample_csv():
    """Analyze a sample CSV if provided"""
    if len(os.sys.argv) > 1:
        csv_path = os.sys.argv[1]
        if os.path.exists(csv_path):
            print_header("CSV FILE ANALYSIS")

            try:
                df = pd.read_csv(csv_path, encoding='utf-8')

                print(f"{Fore.GREEN}File loaded successfully!{Style.RESET_ALL}\n")
                print(f"Total rows: {len(df)}")
                print(f"Unique products: {df['Handle'].nunique()}")
                print(f"Average variants per product: {len(df) / df['Handle'].nunique():.1f}\n")

                print(f"{Fore.CYAN}Available columns:{Style.RESET_ALL}")
                for col in df.columns:
                    print(f"  - {col}")

                print(f"\n{Fore.CYAN}First product:{Style.RESET_ALL}")
                first_handle = df['Handle'].iloc[0]
                first_product = df[df['Handle'] == first_handle]
                print(f"  Handle: {first_handle}")
                if 'Title' in df.columns:
                    print(f"  Title: {first_product['Title'].iloc[0]}")
                if 'Type' in df.columns:
                    print(f"  Type: {first_product['Type'].iloc[0]}")
                print(f"  Variants: {len(first_product)}\n")

            except Exception as e:
                print(f"{Fore.RED}Error reading CSV: {str(e)}{Style.RESET_ALL}")


if __name__ == "__main__":
    demo_translation()
    analyze_sample_csv()
