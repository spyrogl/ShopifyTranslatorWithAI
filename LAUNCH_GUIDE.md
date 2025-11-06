# 🚀 Quick Launch Guide

## Step 1: Launch the GUI

```bash
python run_gui.py
```

## Step 2: You'll See This Interface

```
┌─────────────────────────────────────────────────────────────┐
│  🌍 Shopify Product Translator with AI                      │
├─────────────────────────────────────────────────────────────┤
│ ┌───┬───────┬─────────┬─────┐                              │
│ │📝 │ ☑️     │ ⚙️       │ 📊  │                              │
│ │Setup│Fields│Options │ Log  │                              │
│ └───┴───────┴─────────┴─────┘                              │
│                                                              │
│ ┌─── OpenAI API Configuration ───────────────────────────┐ │
│ │ API Key: ●●●●●●●●●●●●●●●●●●●●   [Get API Key]         │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌─── CSV File Selection ─────────────────────────────────┐ │
│ │ Shopify CSV: /path/to/products.csv  [Browse...]        │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌─── Translation Settings ───────────────────────────────┐ │
│ │ Target Language: [Greek (Ελληνικά) ▼]                  │ │
│ │                                                          │ │
│ │ Mode:                                                    │ │
│ │ ○ Direct Translation                                     │ │
│ │ ● Market Adaptation (Recommended)                       │ │
│ │                                                          │ │
│ │ Model:                                                   │ │
│ │ ● GPT-4o-mini (Fast, $0.001/product)                   │ │
│ │ ○ GPT-4o (Premium, $0.013/product)                     │ │
│ │                                                          │ │
│ │ Special Instructions:                                    │ │
│ │ [Winter clothing for men aged 25-50____________]        │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ [💾 Save Settings]           [📋 Preview] [🚀 Start]         │
└─────────────────────────────────────────────────────────────┘
```

## Step 3: Select Fields (Tab 2)

```
┌─────────────────────────────────────────────────────────────┐
│ Select which fields to translate:                           │
│                                                              │
│ [Select All] [Select Recommended] [Clear All]               │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ ☑ Title                                                 │ │
│ │ ☑ Body (HTML)                                          │ │
│ │ ☑ Type                                                  │ │
│ │ ☐ Tags                                                  │ │
│ │ ☑ Option1 Name                                         │ │
│ │ ☑ Option1 Value                                        │ │
│ │ ☑ Option2 Name                                         │ │
│ │ ☑ Option2 Value                                        │ │
│ │ ☐ Option3 Name                                         │ │
│ │ ☐ Option3 Value                                        │ │
│ │ ☐ Image Alt Text                                       │ │
│ │ ☐ SEO Title                                            │ │
│ │ ☐ SEO Description                                      │ │
│ └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Step 4: Configure Options (Tab 3)

```
┌─────────────────────────────────────────────────────────────┐
│ ┌─── 👟 Shoe Size Conversion ────────────────────────────┐ │
│ │ Convert shoe sizes:                                     │ │
│ │                                                          │ │
│ │ ○ No conversion                                          │ │
│ │ ● US → EU (e.g., US 8 → EU 41)                         │ │
│ │ ○ EU → US (e.g., EU 41 → US 8)                         │ │
│ │                                                          │ │
│ │ ℹ️ Auto-detection:                                       │ │
│ │                                                          │ │
│ │ • Women's: EU 35-42 or keywords (women, γυναικεία)     │ │
│ │ • Men's: EU 39+ or keywords (men, ανδρικά)             │ │
│ │                                                          │ │
│ │ Conversion tables:                                       │ │
│ │ Women's: US 5=EU 35, US 7=EU 37, US 9=EU 39           │ │
│ │ Men's: US 7=EU 40, US 9=EU 42, US 11=EU 44            │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌─── 📁 Output Settings ─────────────────────────────────┐ │
│ │ Output files: translated_outputs/                       │ │
│ │ Backups: backups/                                       │ │
│ └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Step 5: Watch Progress (Tab 4 - Log)

```
┌─────────────────────────────────────────────────────────────┐
│ ✓ API Key validated                                         │
│ ✓ Loading CSV file: products_export.csv                    │
│ ✓ Backup created: backups/backup_20241105_products.csv    │
│ ✓ Analyzing file structure...                              │
│   - Total rows: 18                                          │
│   - Unique products: 1                                      │
│   - Average variants: 18.0                                  │
│                                                              │
│ 🚀 Starting translation process...                         │
│                                                              │
│ Translating: "Elegant winter coat for men"                 │
│ Progress: ████████░░░░░░░░ 42% (8/18)                     │
│ Time remaining: 2 minutes                                   │
│ Cost so far: $0.04                                          │
│                                                              │
│ ✓ Translated Title: Κομψό χειμερινό παλτό για άνδρες     │
│ ✓ Translated Option1 Name: Color → Χρώμα                  │
│ ✓ Translated Option1 Value: Blue → Μπλε                   │
│ ✓ Converted shoe size: US 8 → EU 41 (Men's detected)      │
│                                                              │
│ ✓ Translation completed in 2.3 minutes                     │
│ ✓ Output saved: translated_outputs/products_greek.csv     │
│ Total cost: $0.05 USD                                       │
│                                                              │
│ 🎉 Ready to import to Shopify!                             │
│                                                              │
│ [Clear Log]                                                 │
└─────────────────────────────────────────────────────────────┘
```

## Features at a Glance

### ✨ What You Can Do

1. **Import CSV**: Browse or drag & drop
2. **Select Fields**: Check what to translate
3. **Choose Language**: 6 languages available
4. **Translation Mode**: Direct or Market Adaptation
5. **Shoe Conversion**: US ↔ EU automatic
6. **Preview**: See file structure before translating
7. **Real-time Log**: Watch progress live
8. **Save Settings**: Remember your preferences
9. **Cost Estimate**: See price before starting

### 🎯 Perfect For

- Non-technical users
- Batch translations
- Multiple languages
- Dropshipping stores
- Shoe/fashion products
- Professional branding

## Example Workflow

```bash
# 1. Launch
python run_gui.py

# 2. Setup Tab
- Enter API key
- Browse to products.csv
- Select Greek
- Mode: Market Adaptation
- Model: GPT-4o-mini

# 3. Fields Tab
- Click "Select Recommended"

# 4. Options Tab
- Select "US → EU"

# 5. Click "Start Translation"
- Confirm dialog
- Watch Log tab
- Done!
```

## Result

```csv
# Before
Handle,Title,Option1 Name,Option1 Value,Option2 Name,Option2 Value
winter-coat,Elegant winter coat | Charles,Color,Blue,Size,US 8

# After (Greek)
Handle,Title,Option1 Name,Option1 Value,Option2 Name,Option2 Value
winter-coat,Κομψό χειμερινό παλτό,Χρώμα,Μπλε,Μέγεθος,EU 41
```

✅ **Professional**
✅ **No personal names**
✅ **Consistent option names**
✅ **Converted shoe sizes**
✅ **Ready for Shopify import**

---

## Troubleshooting

**Q: GUI doesn't launch?**
```bash
# Check tkinter
python -c "import tkinter"

# If error:
sudo apt-get install python3-tk  # Ubuntu/Debian
```

**Q: API key error?**
- Get key from: https://platform.openai.com/api-keys
- Ensure billing is set up
- Check for typos

**Q: Shoe sizes not converting?**
- Include gender keywords (men's, women's, ανδρικά, γυναικεία)
- Use format "US 8" or "EU 41"
- Check Log tab for detection results

---

**Ready to translate?** 🚀

```bash
python run_gui.py
```
