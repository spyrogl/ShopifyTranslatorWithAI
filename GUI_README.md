# Shopify Translator GUI 🖥️

Beautiful graphical interface for translating Shopify products with AI and shoe size conversion.

## Features

### 🎨 Modern Interface
- **4 Tabs**: Setup, Fields, Options, Log
- Easy file import with Browse button
- Visual field selection with checkboxes
- Real-time translation log
- Save/load settings

### 🌍 Translation Features
- **6 Languages**: Greek, Dutch, German, French, Spanish, Italian
- **2 Modes**: Direct Translation & Market Adaptation
- **2 Models**: GPT-4o-mini (fast) & GPT-4o (premium)
- **Smart caching**: Automatic translation caching
- **Standard option names**: Consistent Color → Χρώμα, Size → Μέγεθος

### 👟 Shoe Size Conversion (NEW!)
- **US → EU**: Convert US sizes to EU sizes
- **EU → US**: Convert EU sizes to US sizes
- **Auto-detection**:
  - Women's shoes detected by EU 35-42 or keywords (women, ladies, female)
  - Men's shoes detected by EU 39+ or keywords (men, male)
  - Greek keywords supported (ανδρικά, γυναικεία)

**Conversion Tables:**

Women's:
- US 5 = EU 35
- US 6 = EU 36
- US 7 = EU 37
- US 8 = EU 38
- US 9 = EU 39

Men's:
- US 7 = EU 40
- US 8 = EU 41
- US 9 = EU 42
- US 10 = EU 43
- US 11 = EU 44

## Installation

### Prerequisites
- Python 3.8 or higher
- tkinter (usually included with Python)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Verify tkinter Installation

```bash
python -c "import tkinter"
```

If you get an error:
- **Ubuntu/Debian**: `sudo apt-get install python3-tk`
- **Fedora**: `sudo dnf install python3-tkinter`
- **macOS/Windows**: tkinter comes with Python

## Launch the GUI

### Method 1: Using launcher script (Recommended)

```bash
python run_gui.py
```

### Method 2: Direct launch

```bash
python shopify_translator_gui.py
```

### Method 3: Make executable (Linux/Mac)

```bash
chmod +x run_gui.py
./run_gui.py
```

## How to Use

### Tab 1: 📝 Setup

1. **API Key**:
   - Enter your OpenAI API key
   - Click "Get API Key" to open OpenAI website
   - Key is saved automatically

2. **Select CSV File**:
   - Click "Browse..." to select your Shopify export
   - Or drag & drop the file

3. **Translation Settings**:
   - Choose target language (Greek, Dutch, etc.)
   - Select mode:
     - **Direct Translation**: Literal, word-for-word
     - **Market Adaptation**: Localized, SEO-optimized (recommended)
   - Select model:
     - **GPT-4o-mini**: Fast, $0.001/product (recommended)
     - **GPT-4o**: Premium quality, $0.013/product
   - Add special instructions (optional):
     - Example: "Winter clothing for men aged 25-50"

### Tab 2: ☑️ Fields

1. **Quick Selection**:
   - "Select All": Translate all available fields
   - "Select Recommended": Title, Body, Type, Options
   - "Clear All": Deselect everything

2. **Manual Selection**:
   - Check/uncheck individual fields
   - Recommended fields are pre-selected:
     - Title
     - Body (HTML)
     - Type
     - Option1 Name (Color)
     - Option1 Value (Blue, Black, etc.)
     - Option2 Name (Size)
     - Option2 Value (S, M, L, etc.)

### Tab 3: ⚙️ Options

1. **Shoe Size Conversion**:
   - **No conversion**: Keep sizes as-is
   - **US → EU**: Convert US 8 to EU 41
   - **EU → US**: Convert EU 41 to US 8

2. **Auto-detection**:
   - Detects women's vs men's shoes automatically
   - Based on keywords or size ranges
   - See info panel for details

3. **Output Settings**:
   - Translated files saved to: `translated_outputs/`
   - Backups saved to: `backups/`

### Tab 4: 📊 Log

- View real-time translation progress
- See API responses
- Check for errors
- Clear log button available

### Bottom Buttons

- **💾 Save Settings**: Save current configuration
- **📋 Preview**: Preview CSV file structure
- **🚀 Start Translation**: Begin translation process

## Workflow Example

### Scenario: Translate 50 Winter Coats to Greek with Shoe Sizes

1. **Setup Tab**:
   - Enter API key
   - Browse to `winter_coats.csv`
   - Select "Greek (Ελληνικά)"
   - Mode: Market Adaptation
   - Model: GPT-4o-mini
   - Instructions: "Winter clothing for men, emphasize warmth"

2. **Fields Tab**:
   - Click "Select Recommended"
   - Ensure Option Names and Values are checked

3. **Options Tab**:
   - Select "US → EU" for shoe size conversion
   - (System will auto-detect gender)

4. **Click "Start Translation"**:
   - Confirm dialog shows estimate
   - Watch progress in Log tab
   - Wait for completion

5. **Result**:
   - File saved: `translated_outputs/winter_coats_greek_20241105.csv`
   - Ready to import to Shopify
   - Shoe sizes converted
   - Option names in Greek

## Keyboard Shortcuts

- **Ctrl+S**: Save settings
- **Ctrl+O**: Open file browser
- **Ctrl+L**: Clear log
- **F5**: Refresh/Preview file

## Troubleshooting

### "tkinter is not installed"

Install tkinter for your OS:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# macOS/Windows
# tkinter comes pre-installed with Python
```

### "API key validation failed"

1. Check your API key at https://platform.openai.com/api-keys
2. Ensure you have billing set up
3. Try creating a new API key

### "Could not read CSV file"

1. Ensure it's a valid Shopify CSV export
2. Check file encoding is UTF-8
3. Try re-exporting from Shopify

### GUI doesn't launch

1. Verify Python version: `python --version` (should be 3.8+)
2. Check dependencies: `pip install -r requirements.txt`
3. Try: `python run_gui.py --debug`

### Shoe sizes not converting

1. Check product description contains gender keywords
2. Ensure shoe sizes are in format "US 8" or "EU 41"
3. Check Log tab for detection results

## Advanced Features

### Batch Processing

1. Load first CSV file
2. Configure all settings
3. Click "Save Settings"
4. For each additional file:
   - Load new CSV
   - Click "Start Translation" (settings are saved)

### Custom Shoe Size Ranges

Edit `shoe_size_converter.py` to add custom sizes:

```python
WOMENS_SHOE_SIZES = {
    4: 34,
    # Add your custom sizes here
    12.5: 42.5,
}
```

### Multi-language Export

To translate same catalog to multiple languages:

1. Translate to Greek → Save
2. Load same original CSV again
3. Change language to Dutch
4. Translate → Save
5. Repeat for all languages

## File Structure

```
ShopifyTranslatorWithAI/
├── shopify_translator_gui.py      # GUI application
├── run_gui.py                      # Launcher script
├── shopify_translator.py           # Core translator
├── shoe_size_converter.py          # Shoe size logic
├── config.json                     # Saved settings
├── translation_cache.json          # Translation cache
├── backups/                        # Original files
└── translated_outputs/             # Translated files
```

## Tips for Best Results

1. **Start Small**: Test with 1-2 products first
2. **Use Market Adaptation**: For natural-sounding translations
3. **Add Context**: Special instructions improve quality
4. **Check Log**: Monitor for errors or warnings
5. **Preview First**: Use Preview button to verify file structure
6. **Save Settings**: Save your preferred configuration
7. **Shoe Detection**: Include gender keywords for better detection

## Cost Examples

Using GPT-4o-mini:

| Products | Estimated Cost |
|----------|---------------|
| 1 product | $0.001 |
| 10 products | $0.01 - $0.05 |
| 50 products | $0.03 - $0.10 |
| 100 products | $0.10 - $0.50 |
| 500 products | $0.50 - $2.50 |

## Support

- **GitHub Issues**: Report bugs or feature requests
- **Documentation**: See README.md for full details
- **OpenAI Status**: https://status.openai.com

## Credits

Built with:
- **Python tkinter**: GUI framework
- **OpenAI GPT**: Translation engine
- **pandas**: CSV processing
- **Custom shoe converter**: Size conversion logic

---

**Made with ❤️ for dropshipping entrepreneurs** 🇬🇷🚀
