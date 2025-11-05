# Shopify Product Translator with AI

Translate your Shopify product catalogs into multiple languages using OpenAI's GPT models with intelligent market adaptation.

## Features

- **Multiple Languages**: Greek, Dutch, German, French, Spanish, Italian (easily extensible)
- **Two Translation Modes**:
  - **Direct Translation**: Literal, word-for-word translations
  - **Market Adaptation**: Localized, culturally-adapted translations optimized for each market
- **Cost-Effective**: Uses GPT-4o-mini by default (~$0.001 per product)
- **Smart Caching**: Automatically caches translations to avoid re-translating common terms
- **HTML Preservation**: Maintains all HTML formatting in product descriptions
- **Variant Intelligence**: Understands Shopify's variant structure (colors, sizes)
- **Real-Time Tracking**: Progress bars and cost estimates throughout the process
- **Safe & Reliable**:
  - Automatic backups before translation
  - Error handling with fallback to original text
  - Resume capability through caching
  - Output validation

## Requirements

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Shopify product export CSV file

## Installation

```bash
# Clone or download this repository
cd ShopifyTranslatorWithAI

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

### 1. Try the Demo (No API Key Required)

```bash
python demo.py
```

This shows sample translations without using any API credits.

### 2. Run Your First Translation

```bash
python shopify_translator.py products_export.csv
```

Follow the interactive prompts to:
1. Enter your OpenAI API key
2. Review file analysis
3. Select fields to translate
4. Choose target language and settings
5. Review cost estimate
6. Start translation

## Usage Guide

### Basic Usage

```bash
python shopify_translator.py path/to/your/products.csv
```

### Interactive Workflow

The translator guides you through 8 steps:

1. **API Configuration**: Enter and validate your OpenAI API key
2. **Load CSV**: Automatic backup creation
3. **File Analysis**: Shows products, variants, and available fields
4. **Field Selection**: Choose which fields to translate
5. **Translation Settings**: Language, mode, model selection
6. **Cost Estimate**: Preview costs before starting
7. **Translation Process**: Real-time progress tracking
8. **Save Results**: Validated output ready for Shopify import

### Translation Modes

#### Direct Translation
Best for: Product attributes, colors, sizes, categories
- Literal, accurate translations
- Fast and consistent
- Lower temperature (0.3) for consistency

#### Market Adaptation (Recommended)
Best for: Product titles, descriptions, marketing content
- Culturally adapted language
- SEO-optimized for target market
- Natural phrasing for native speakers
- Market-specific persuasive tone

### Supported Languages

| Language | Native Name | Market Adaptation |
|----------|-------------|-------------------|
| Greek | Ελληνικά | Formal, quality-focused |
| Dutch | Nederlands | Direct, practical |
| German | Deutsch | Professional, precise |
| French | Français | Sophisticated, elegant |
| Spanish | Español | Warm, family-oriented |
| Italian | Italiano | Stylish, expressive |

### Model Selection

#### GPT-4o-mini (Recommended)
- **Cost**: ~$0.001 per product
- **Quality**: Excellent for e-commerce
- **Speed**: Fast
- **Best for**: 95% of translations

#### GPT-4o (Premium)
- **Cost**: ~$0.013 per product
- **Quality**: Outstanding, nuanced
- **Speed**: Slightly slower
- **Best for**: Luxury products, complex descriptions

### Cost Estimates

| Products | Model | Estimated Cost |
|----------|-------|----------------|
| 1 product | GPT-4o-mini | $0.001 |
| 50 products | GPT-4o-mini | $0.03 - $0.05 |
| 100 products | GPT-4o-mini | $0.10 - $0.50 |
| 500 products | GPT-4o-mini | $0.50 - $2.50 |

## Field Selection

### Always Translate
- Title
- Body (HTML) - Descriptions
- Type - Product category

### Often Translate
- Option1 Value - Usually colors
- Tags - Product tags
- Image Alt Text - SEO descriptions
- SEO Title
- SEO Description

### Never Translate
- Handle
- Prices
- SKUs
- Image URLs
- Barcodes
- Standard sizes (S, M, L, XL, 2XL, 3XL)

## File Structure

After running the translator:

```
ShopifyTranslatorWithAI/
├── shopify_translator.py          # Main application
├── demo.py                         # Demo script
├── requirements.txt                # Dependencies
├── config.json                     # API key (auto-created)
├── translation_cache.json          # Cached translations
├── products_export.csv             # Your source file
├── backups/                        # Automatic backups
│   └── backup_20241105_products.csv
└── translated_outputs/             # Translated files
    └── products_greek_20241105.csv
```

## Special Instructions Examples

### Winter Clothing
```
These are winter coats and jackets. Emphasize warmth, weather
protection, insulation quality, and seasonal style. Mention
suitability for cold European winters.
```

### Men's Fashion
```
Target audience: men aged 25-50 interested in stylish, quality
clothing. Emphasize timeless design, versatility, and how the
item fits into a modern wardrobe. Use confident, masculine tone.
```

### Luxury Items
```
Premium, high-end products. Use refined, sophisticated language.
Emphasize craftsmanship, quality materials, and exclusivity.
Appeal to discerning customers who value excellence.
```

## Troubleshooting

### API Key Issues

**Problem**: "API key validation failed"

**Solution**:
1. Check your API key at https://platform.openai.com/api-keys
2. Ensure you have billing set up on OpenAI
3. Verify the key has no extra spaces

### CSV Loading Issues

**Problem**: "Could not read CSV file"

**Solution**:
1. Ensure file is a valid Shopify CSV export
2. Check file is UTF-8 encoded
3. Verify file path is correct

### Rate Limits

**Problem**: "Rate limit exceeded"

**Solution**:
- The translator automatically adds 0.5s delays between requests
- If you hit limits, wait a few minutes and resume
- Translation cache preserves your progress

### HTML Breaking

**Problem**: HTML tags are malformed after translation

**Solution**:
- The translator includes HTML preservation logic
- If issues persist, use "Direct Translation" mode for HTML fields
- Original text is preserved if translation fails validation

## Advanced Features

### Translation Caching

Common terms are cached automatically:
- Colors (Blue, Black, White, etc.)
- Sizes (S, M, L, XL, etc.)
- Product types (Jackets, Shirts, etc.)
- Common phrases

Cache is saved to `translation_cache.json` and shared across sessions.

### Resume Capability

If translation is interrupted:
1. Cache is automatically saved every 10 products
2. Re-run the same command
3. Cached translations will be used (no additional cost)

### Batch Processing

To translate to multiple languages:

```bash
# Translate to Greek
python shopify_translator.py products.csv
# Select Greek, complete translation

# Translate to Dutch (using cache)
python shopify_translator.py products.csv
# Select Dutch, cached colors/sizes reused
```

## Configuration

Default settings are saved to `config.json`:

```json
{
  "openai_api_key": "sk-...",
  "default_language": "greek",
  "default_mode": "market_adaptation",
  "default_model": "gpt-4o-mini"
}
```

Edit this file to change defaults or remove it to reset.

## Import to Shopify

After translation:

1. Go to Shopify Admin > Products
2. Click "Import"
3. Upload the translated CSV from `translated_outputs/`
4. Select "Overwrite existing products with same handle"
5. Review and confirm import

## Best Practices

1. **Start Small**: Test with 1-2 products first
2. **Review Quality**: Check first translation before processing hundreds
3. **Use Market Adaptation**: For descriptions and marketing content
4. **Cache Common Terms**: Pre-translate colors/sizes once
5. **Backup Regularly**: Keep backups of your original CSVs
6. **Monitor Costs**: Check estimates before large batches

## Cost Optimization Tips

1. **Use GPT-4o-mini**: 95% the quality at 1/10th the cost
2. **Enable Caching**: Automatically enabled, saves on repeated terms
3. **Select Only Needed Fields**: Don't translate fields you don't need
4. **Batch Similar Products**: Translations in same session reuse cache
5. **Use Direct Mode for Simple Fields**: Categories, colors, sizes

## License

MIT License - Free for personal and commercial use

## Support

For issues, questions, or contributions:
- Create an issue on GitHub
- Check OpenAI status: https://status.openai.com
- Review OpenAI docs: https://platform.openai.com/docs

## Credits

Built with:
- OpenAI GPT models for translation
- pandas for CSV processing
- colorama for beautiful terminal output
- tqdm for progress tracking

---

Made with ❤️ for dropshipping entrepreneurs and e-commerce businesses worldwide.
