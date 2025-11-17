# 🖥️ Shopify Translator - CLI Mode Guide

## Quick Start (Windows Terminal)

### Step 1: Setup Your API Key (ONE TIME)

Double-click `setup_api_key.bat` or run:
```cmd
setup_api_key.bat
```

**Get your API key from:** https://platform.openai.com/api-keys

---

### Step 2: Run Translation

Drag your CSV file onto `translate.bat` or run:
```cmd
translate.bat products.csv
```

Or with full path:
```cmd
translate.bat "C:\Users\Desktop\products.csv"
```

---

## ✨ What You'll See

The CLI will ask you:

1. **Target Language** - Type: `greek`, `spanish`, `french`, etc.
2. **Translation Mode** - Press Enter for default (market_adaptation)
3. **Model** - Press Enter for default (gpt-4o-mini)
4. **Fields to Translate** - Press Enter for recommended fields
5. **Special Instructions** - Optional, press Enter to skip
6. **Shoe Conversion** - Type: `none`, `us_to_eu`, or `eu_to_us`
7. **Confirm** - Type `yes` to start

---

## 📂 Output Location

Your translated file will be saved in:
```
translated_outputs/TranslatedWithAI{count}{date}{time}.csv
```

Example: `TranslatedWithAI10171120251553.csv`

---

## 🔑 Troubleshooting

### Error 401: Invalid API Key

**Solution:**
1. Go to: https://platform.openai.com/api-keys
2. Create a NEW API key
3. Run `setup_api_key.bat` again
4. Paste the new key

### Error: Python not found

**Solution:**
Install Python from: https://www.python.org/downloads/

Make sure to check "Add Python to PATH" during installation.

### Error: CSV file not found

**Solution:**
- Use full path in quotes: `"C:\Users\Desktop\products.csv"`
- Make sure the file exists

---

## 💡 Pro Tips

### Skip Questions (Auto Mode)

Create a file called `auto_translate.bat`:
```batch
@echo off
python shopify_translator.py %1 --auto --language greek --mode market_adaptation
```

### Batch Process Multiple Files

Create `batch_translate.bat`:
```batch
@echo off
for %%f in (*.csv) do (
    echo Processing %%f...
    python shopify_translator.py "%%f"
)
```

---

## 📋 Available Languages

greek, spanish, french, german, italian, portuguese, dutch, russian, polish, turkish, japanese, chinese, korean, arabic, swedish, danish, norwegian, finnish, czech, hungarian, romanian, bulgarian, croatian, slovak, ukrainian, hebrew, thai, vietnamese, indonesian, malay, hindi, bengali, tamil, telugu, marathi, gujarati, kannada, malayalam, punjabi, urdu, persian, swahili, amharic, yoruba, igbo, zulu, afrikaans, albanian, armenian, azerbaijani, basque, belarusian, bosnian, catalan, estonian, filipino, galician, georgian, haitian, icelandic, irish, kazakh, khmer, lao, latvian, lithuanian, macedonian, maltese, mongolian, nepali, pashto, serbian, sinhala, slovenian, somali, sundanese, tajik, uzbek, welsh, xhosa, yiddish, esperanto, latin

---

## 🆘 Need Help?

Run without arguments to see help:
```cmd
python shopify_translator.py
```

Or check the main README: `README.md`

---

## 🚀 Advanced Usage

### Custom Settings

Edit `config.json` manually:
```json
{
  "openai_api_key": "sk-your-key-here",
  "default_language": "greek",
  "default_model": "gpt-4o-mini",
  "default_mode": "market_adaptation"
}
```

### Debug Mode

Add `--debug` flag:
```cmd
python shopify_translator.py products.csv --debug
```

---

**Enjoy your translations!** 🎉
