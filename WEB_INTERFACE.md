# 🌐 Web Interface Guide

Beautiful, modern web interface for the Shopify Product Translator - use it directly in your browser!

## Features

✨ **Modern Design**
- Beautiful gradient interface
- Responsive layout (works on all devices)
- Intuitive 4-tab navigation
- Real-time progress tracking
- Professional appearance

🚀 **Easy to Use**
- No technical knowledge required
- Drag & drop file upload
- Visual field selection
- One-click translation
- Automatic file download

📊 **Full Features**
- All 7 languages supported
- Cost estimation before translation
- Real-time progress updates
- Shoe size conversion
- 4 bullet point format
- Complete customization

## Quick Start

### Installation

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Launch the web interface:**
```bash
python run_web.py
```

3. **Your browser will open automatically** to `http://localhost:5000`

That's it! 🎉

## Using the Web Interface

### Tab 1: 📝 Setup

1. **Upload CSV File**
   - Click the upload area or drag & drop your Shopify CSV
   - File is analyzed automatically
   - See total products and available fields

2. **Enter API Key**
   - Paste your OpenAI API key
   - Click the link to get one if you don't have it

3. **Select Target Language**
   - Choose from dropdown (7 languages)
   - Default: Greek

4. **Choose Translation Mode**
   - Direct Translation: Literal translations
   - Market Adaptation: Localized, SEO-optimized ✓ Recommended

5. **Select AI Model**
   - GPT-4o-mini: Fast & economical (~$0.001/product) ✓ Recommended
   - GPT-4o: Premium quality (~$0.013/product)

6. **Add Special Instructions** (Optional)
   - Example: "Winter clothing for men aged 25-50"

### Tab 2: ☑️ Fields

Select which fields to translate:

- **Quick buttons:**
  - Select All: Check all fields
  - Recommended: Title, Body, Type, Options
  - Clear All: Uncheck everything

- **Manual selection:**
  - Click individual checkboxes
  - Grayed out fields are not available in your CSV

**Recommended fields:**
- ✓ Title
- ✓ Body (HTML)
- ✓ Type
- ✓ Option1 Name
- ✓ Option1 Value
- ✓ Option2 Name
- ✓ Option2 Value

### Tab 3: ⚙️ Options

1. **Shoe Size Conversion**
   - No conversion (default)
   - US → EU (e.g., US 8 → EU 41)
   - EU → US (e.g., EU 41 → US 8)

2. **Auto-detection info:**
   - Women's shoes: EU 35-42 or keywords
   - Men's shoes: EU 39+ or keywords
   - Conversion tables provided

3. **Description Format**
   - Automatic 4 bullet points format
   - Applies to Body (HTML) field
   - Proven to increase conversions

### Tab 4: 🚀 Translate

1. **Review Summary**
   - See all your settings
   - Cost estimate displayed
   - Verify everything is correct

2. **Click "Start Translation"**
   - Confirmation dialog
   - Real-time progress bar
   - Status messages
   - Token count and cost tracking

3. **Download Result**
   - When complete, download button appears
   - File saved to `translated_outputs/`
   - Ready to import to Shopify

## Visual Walkthrough

### Interface Preview

```
┌─────────────────────────────────────────────────────────────┐
│  🌍 Shopify Product Translator                              │
│  Translate your products to 7 languages with AI             │
├─────────────────────────────────────────────────────────────┤
│ [📝 Setup] [☑️ Fields] [⚙️ Options] [🚀 Translate]          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Step 1: Upload CSV File                                    │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  📁 Click to upload Shopify CSV file                   │ │
│  │     or drag and drop here                              │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ✓ File Loaded                                              │
│  File: products.csv                                         │
│  Total Rows: 18                                             │
│  Products: 1                                                │
│                                                              │
│  Step 2: API Key                                            │
│  OpenAI API Key: [●●●●●●●●●●●●●●●●●●●●]                    │
│                                                              │
│  Step 3: Target Language                                    │
│  [Español Chileno (Chilean Spanish) ▼]                     │
│                                                              │
│  Step 4: Translation Mode                                   │
│  ○ Direct Translation                                       │
│  ● Market Adaptation (Recommended)                          │
│                                                              │
│  Step 5: AI Model                                           │
│  ● GPT-4o-mini (~$0.001/product)                           │
│  ○ GPT-4o (~$0.013/product)                                │
│                                                              │
│  Special Instructions (Optional)                            │
│  [Winter clothing for men aged 25-50____________]          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Progress Screen

```
┌─────────────────────────────────────────────────────────────┐
│  Translation Progress                                        │
│                                                              │
│  Translating product 8/10...                                │
│                                                              │
│  [████████████████████░░░░░░] 80%                          │
│                                                              │
│  Processing...                                              │
└─────────────────────────────────────────────────────────────┘
```

### Completion Screen

```
┌─────────────────────────────────────────────────────────────┐
│  ✓ Translation Completed!                                    │
│                                                              │
│  Output File: products_chilean_20241107.csv                 │
│  Total Tokens: 1,234                                        │
│  Total Cost: $0.05 USD                                      │
│                                                              │
│  Ready to import to Shopify!                                │
│                                                              │
│  [📥 Download Translated File]                              │
└─────────────────────────────────────────────────────────────┘
```

## Advantages Over GUI/CLI

### Why Use Web Interface?

✅ **No Installation Issues**
- No tkinter required
- Works on any operating system
- Just needs Python + Flask

✅ **Better User Experience**
- Modern, beautiful design
- Drag & drop upload
- Visual feedback
- Progress animations

✅ **Remote Access**
- Run on server, access from any device
- Team collaboration possible
- Cloud deployment ready

✅ **Mobile Friendly**
- Responsive design
- Works on tablets and phones
- Touch-optimized

✅ **Professional Appearance**
- Client-ready interface
- Beautiful gradients and styling
- Modern web standards

## Technical Details

### Architecture

**Frontend:**
- HTML5
- CSS3 (modern features)
- Vanilla JavaScript (no frameworks)
- Responsive design

**Backend:**
- Flask web framework
- RESTful API
- Background task processing
- File upload handling

### API Endpoints

```
GET  /                       - Main interface
GET  /api/languages          - Get available languages
GET  /api/fields             - Get translatable fields
POST /api/upload             - Upload CSV file
POST /api/estimate           - Estimate translation cost
POST /api/translate          - Start translation
GET  /api/progress/:id       - Check translation progress
GET  /api/download/:filename - Download result
```

### File Structure

```
ShopifyTranslatorWithAI/
├── web_interface.html      # Main HTML interface
├── web_server.py           # Flask server
├── run_web.py              # Launcher script
├── uploads/                # Uploaded CSV files
├── translated_outputs/     # Translated files
└── backups/                # Backup files
```

## Configuration

### Change Port

Edit `web_server.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8000)  # Change 5000 to 8000
```

### Enable Remote Access

Default: `localhost` only

To allow other devices:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

Then access from other devices:
```
http://YOUR_IP_ADDRESS:5000
```

### Production Deployment

For production use:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

Or use a production server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 web_server:app
```

## Troubleshooting

### Port Already in Use

**Error:** "Address already in use"

**Solution:**
1. Change port in `web_server.py`
2. Or kill process using port 5000:
```bash
# Linux/Mac
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Browser Doesn't Open

**Solution:**
1. Wait a few seconds
2. Manually open: http://localhost:5000
3. Check firewall settings

### File Upload Error

**Solution:**
1. Check file size (max 16MB)
2. Ensure file is CSV format
3. Check file permissions
4. Try different browser

### Translation Stalls

**Solution:**
1. Check browser console (F12)
2. Verify API key is correct
3. Check OpenAI account has credits
4. Reload page and try again

## Security Notes

### Important

- ⚠️ **API keys are stored temporarily** on the server
- ⚠️ **Use HTTPS** for production
- ⚠️ **Don't expose** to public internet without authentication
- ⚠️ **Clear uploaded files** periodically

### Best Practices

1. **Local use only** (recommended)
2. **Use environment variables** for API keys
3. **Add authentication** for shared servers
4. **Enable HTTPS** for remote access
5. **Set up firewall rules**

## Examples

### Example 1: Quick Translation

1. Launch: `python run_web.py`
2. Upload: `products.csv`
3. API Key: Paste your key
4. Language: Chilean
5. Click "Translate" tab
6. Click "Start Translation"
7. Download when complete

**Time:** ~2 minutes for 10 products

### Example 2: Batch Processing

1. Upload multiple CSVs one by one
2. Same settings for all
3. Download each result
4. Import all to Shopify

### Example 3: Testing

1. Use sample `products_export.csv`
2. Select just Title field
3. Use GPT-4o-mini
4. Check result quality
5. Scale up to all fields

## Comparison

### Web vs GUI vs CLI

| Feature | Web | GUI | CLI |
|---------|-----|-----|-----|
| Easy to use | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Beautiful interface | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐ |
| No dependencies | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Remote access | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ |
| Mobile friendly | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ |
| Speed | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**Recommendation:**
- **Non-technical users:** Web Interface
- **Technical users:** CLI
- **Team use:** Web Interface
- **Automation:** CLI

## Updates

### Auto-refresh

The interface automatically refreshes data:
- File analysis: Immediate
- Cost estimate: On settings change
- Progress: Every 1 second
- No manual refresh needed

### Real-time Features

- ✅ Progress bar updates live
- ✅ Status messages update
- ✅ Token count tracked
- ✅ Cost calculated in real-time

## Support

### Getting Help

1. Check browser console (F12)
2. Check server console output
3. Review error messages
4. Check this documentation
5. Verify API key and credits

### Common Issues

**Q: Interface looks broken**
- Clear browser cache
- Try different browser
- Check CSS loaded correctly

**Q: Slow performance**
- Check server resources
- Reduce file size
- Use faster model (GPT-4o-mini)

**Q: Can't download result**
- Check file exists in `translated_outputs/`
- Try right-click → Save As
- Check browser download settings

## Summary

### What You Get

1. 🌐 **Beautiful web interface**
2. 📱 **Mobile-friendly design**
3. 🚀 **Easy to use**
4. 💰 **Cost estimation**
5. 📊 **Real-time progress**
6. 📥 **One-click download**
7. 🌍 **7 languages**
8. 👟 **Shoe conversion**
9. 📝 **4 bullet format**
10. ✨ **Professional results**

### Quick Commands

```bash
# Install
pip install -r requirements.txt

# Launch
python run_web.py

# Access
http://localhost:5000
```

---

**Ready to translate?** 🚀

```bash
python run_web.py
```

Your browser will open automatically with the beautiful web interface!
