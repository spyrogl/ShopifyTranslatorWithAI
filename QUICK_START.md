# Quick Start Guide

Get your Shopify products translated in 5 minutes!

## Prerequisites

- Python 3.8+ installed ([Download here](https://www.python.org/downloads/))
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Shopify product export CSV

## Step 1: Get Your OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-...`)
5. Add billing info if you haven't already

**Note**: You'll need a few dollars in your OpenAI account. 100 products costs approximately $0.10-$0.50.

## Step 2: Export Products from Shopify

1. Log into your Shopify Admin
2. Go to **Products** > **All products**
3. Click **Export**
4. Select **All products** or **Selected products**
5. Format: **CSV for Excel, Numbers, or other spreadsheet programs**
6. Export: **All product details**
7. Click **Export products**
8. Download the CSV file

## Step 3: Install the Translator

### Option A: Quick Install (Recommended)

```bash
# Navigate to the translator folder
cd ShopifyTranslatorWithAI

# Install dependencies
pip install -r requirements.txt
```

### Option B: Manual Install

```bash
pip install openai pandas openpyxl colorama tqdm
```

### Verify Installation

```bash
python demo.py
```

You should see colorful output showing sample translations.

## Step 4: Run Your First Translation

### Basic Command

```bash
python shopify_translator.py path/to/your/products_export.csv
```

### Example with Sample File

```bash
python shopify_translator.py products_export.csv
```

## Step 5: Follow the Interactive Prompts

### Prompt 1: API Key
```
Enter your OpenAI API key: sk-...
```
Paste your OpenAI API key and press Enter.

### Prompt 2: File Analysis
Review the analysis showing:
- Number of products
- Number of variants
- Preview of first product

### Prompt 3: Field Selection
```
Select fields:
```

**Options**:
- Type `all` for all fields
- Type `basic` for Title and Description only
- Press Enter for recommended fields (Title, Description, Type, Colors)
- Type numbers: `1,2,3,5` for specific fields

**Recommended for first run**: Just press Enter

### Prompt 4: Target Language
```
Select language:
```

**Options**:
- Type the language name: `greek`, `dutch`, `german`, etc.
- Type the number: `1` for Greek, `2` for Dutch, etc.
- Press Enter for Greek (default)

**For your use case**: Type `greek` or `1`

### Prompt 5: Translation Mode
```
Select mode (1 or 2):
```

**Options**:
- `1` - Direct Translation (literal)
- `2` - Market Adaptation (recommended) ← **Choose this**

**Recommended**: Press Enter for Market Adaptation

### Prompt 6: Model Selection
```
Select model (1 or 2):
```

**Options**:
- `1` - GPT-4o-mini (recommended, ~$0.001/product) ← **Choose this**
- `2` - GPT-4o (premium, ~$0.013/product)

**Recommended**: Press Enter for GPT-4o-mini

### Prompt 7: Special Instructions
```
Enter special instructions:
```

**For winter coats**:
```
These are winter coats and jackets. Emphasize warmth, weather protection, and style for cold European winters. Target audience: men aged 25-50.
```

Or just press Enter to skip.

### Prompt 8: Cost Estimate & Confirmation
```
Products to translate: 1
Estimated cost: $0.001 USD
Estimated time: 0-1 minutes

Proceed? (yes/no):
```

Type `yes` and press Enter to start.

### Step 6: Watch the Progress

You'll see:
```
Progress: [████████░░] 80% | 8/10 [00:15<00:03]
Current: "Elegant winter coat for men | Charles"
```

### Step 7: Get Your Translated File

When complete, you'll see:
```
✓ Translation Complete!

Output file: translated_outputs/products_export_greek_20241105.csv
Total tokens: 1,234
Total cost: $0.002 USD

Ready to import to Shopify!
```

## Step 8: Import Back to Shopify

1. Go to Shopify Admin > **Products**
2. Click **Import**
3. Click **Add file** and select your translated CSV from `translated_outputs/`
4. Select **Overwrite existing products that have the same handle**
5. Click **Upload and continue**
6. Review the preview
7. Click **Import products**

## Common First-Time Scenarios

### Scenario 1: Testing with Sample File

```bash
# Use the included sample
python shopify_translator.py products_export.csv

# When prompted:
# - Fields: Press Enter (recommended)
# - Language: greek
# - Mode: Press Enter (market adaptation)
# - Model: Press Enter (GPT-4o-mini)
# - Instructions: "Winter fashion for men"
# - Confirm: yes
```

**Expected**: 1 product translated in ~30 seconds, cost ~$0.001

### Scenario 2: Your Own Products (Small Batch)

```bash
# Export 5-10 products from Shopify first
python shopify_translator.py my_products.csv

# Same settings as above
```

**Expected**: 10 products in ~1-2 minutes, cost ~$0.01-$0.05

### Scenario 3: Full Catalog

```bash
# Export all products from Shopify
python shopify_translator.py all_products.csv

# Review estimate carefully!
```

**Expected**: 100 products in ~5-10 minutes, cost ~$0.10-$0.50

## Troubleshooting

### "API key validation failed"
- Check your key at https://platform.openai.com/api-keys
- Ensure billing is set up on OpenAI
- Try creating a new key

### "Could not read CSV file"
- Make sure you exported from Shopify (not from another source)
- Check the file path is correct
- Try dragging and dropping the file path

### "Rate limit exceeded"
- Wait 1-2 minutes
- Your progress is saved in cache
- Re-run the same command

### Translation looks weird
- Try Direct Translation mode for simple fields
- Add more specific instructions
- Review your target audience in special instructions

## Tips for Best Results

1. **Start with 1 product** to verify quality
2. **Use Market Adaptation** for descriptions (sounds natural)
3. **Add special instructions** about your products (e.g., "luxury watches" or "casual streetwear")
4. **Review first translation** before doing all products
5. **Keep your cache file** to save money on repeated translations

## Cost Examples (GPT-4o-mini)

| Your Catalog | Estimated Cost |
|--------------|----------------|
| 1 product | $0.001 |
| 10 products | $0.01 - $0.05 |
| 50 products | $0.03 - $0.10 |
| 100 products | $0.10 - $0.50 |
| 500 products | $0.50 - $2.50 |

## Next Steps

After your first successful translation:

1. **Review the output** in Excel or Google Sheets
2. **Test import** to a test Shopify store if available
3. **Try other languages** (Dutch, German) using the same CSV
4. **Scale up** to your full catalog

## Need Help?

- Run `python demo.py` to see sample translations
- Check README.md for full documentation
- Review your config.json for saved settings
- Check translation_cache.json to see cached terms

## Quick Reference Card

```bash
# Demo mode (no API cost)
python demo.py

# Basic translation
python shopify_translator.py products.csv

# Analyze CSV without translating
python demo.py products.csv

# Files created:
# - config.json (your API key)
# - translation_cache.json (cached translations)
# - backups/ (original files)
# - translated_outputs/ (results)
```

---

**You're ready to go!** 🚀

Start with the sample file to see how it works:
```bash
python shopify_translator.py products_export.csv
```
