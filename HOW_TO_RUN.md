# 🚀 How to Run the Shopify Translator

## For Windows Users - Exact Steps

### Step 1: Find Your Project Location

First, you need to know where the project is located. It could be in:
- `C:\Users\YourName\ShopifyTranslatorWithAI`
- `C:\Projects\ShopifyTranslatorWithAI`
- `Desktop\ShopifyTranslatorWithAI`

**To find it:**
1. Open Windows Explorer (Windows Key + E)
2. Use the search box and search for "ShopifyTranslatorWithAI"
3. Note the full path where it's located

### Step 2: Open Command Prompt

1. Press `Windows Key + R`
2. Type `cmd` and press Enter
3. A black command prompt window will open

### Step 3: Navigate to the Project

In the command prompt, type the following (replace with YOUR actual path):

```bash
cd C:\Users\YourName\ShopifyTranslatorWithAI
```

For example, if the project is on your Desktop:
```bash
cd C:\Users\kossp\Desktop\ShopifyTranslatorWithAI
```

**To verify you're in the right place, type:**
```bash
dir
```

You should see files like:
- web_interface.html
- web_server.py
- run_web.py
- shopify_translator.py

### Step 4: Install Requirements (First Time Only)

If this is your first time running the program, install the required packages:

```bash
pip install -r requirements.txt
```

Wait for it to complete. You only need to do this once.

### Step 5: Run the Web Interface

Now, simply type:

```bash
python run_web.py
```

**What will happen:**
1. The program will start a web server
2. Your default browser will automatically open
3. You'll see the beautiful web interface at `http://localhost:5000`

### Step 6: Use the Web Interface

Once the browser opens:

1. **Tab 1 - Setup:**
   - Click "Upload CSV" and select your Shopify products file
   - Enter your OpenAI API key
   - Choose target language (Greek, Chilean, Dutch, German, etc.)
   - Select translation mode (Market Adaptation recommended)
   - Select AI model (GPT-4o-mini recommended for cost)

2. **Tab 2 - Fields:**
   - Click "Recommended" to select the most important fields
   - Or manually select which fields to translate

3. **Tab 3 - Options:**
   - Choose shoe size conversion if needed (US → EU or EU → US)
   - 4 bullet point format is automatically applied

4. **Tab 4 - Translate:**
   - Review your settings
   - See cost estimate
   - Click "Start Translation"
   - Watch the progress bar
   - Download your translated file when complete!

### Step 7: Stop the Server

When you're done:
1. Go back to the command prompt window
2. Press `Ctrl + C` to stop the server
3. Type `exit` to close the command prompt

---

## Quick Reference - Three Ways to Use

### 1. Web Interface (Easiest - Recommended for You!)
```bash
python run_web.py
```
Opens browser automatically → Beautiful interface → Easy to use

### 2. GUI Interface (Desktop App)
```bash
python run_gui.py
```
Opens desktop window → Visual interface → No browser needed

### 3. Command Line (Advanced)
```bash
python shopify_translator.py
```
Text-based interface → Faster for experts → More control

---

## Troubleshooting

### "python is not recognized"
- **Solution:** Install Python from python.org
- Make sure to check "Add Python to PATH" during installation

### "No such file or directory"
- **Solution:** You're not in the project folder
- Go back to Step 3 and navigate to the correct location
- Use `dir` command to verify you can see the files

### "No module named flask"
- **Solution:** Run the install command again:
```bash
pip install -r requirements.txt
```

### "Port 5000 already in use"
- **Solution:** Close any other programs using port 5000
- Or change the port in `web_server.py` (line 322) to 8000

### Browser doesn't open automatically
- **Solution:** Manually open your browser and go to:
```
http://localhost:5000
```

---

## Example Session

```
C:\Users\kossp> cd Desktop\ShopifyTranslatorWithAI

C:\Users\kossp\Desktop\ShopifyTranslatorWithAI> python run_web.py

======================================================================
🌍 Shopify Product Translator - Web Interface
======================================================================

📊 Starting web server...
🌐 Your browser will open automatically
⚡ Press Ctrl+C to stop the server

======================================================================

* Running on http://127.0.0.1:5000
* Browser opening...
```

Then your browser opens and you can start translating!

---

## Need Help?

1. Make sure Python is installed: `python --version`
2. Make sure pip is working: `pip --version`
3. Make sure you're in the right folder: `dir` should show the files
4. Make sure dependencies are installed: `pip list | findstr flask`

**Still stuck?** Check the other documentation files:
- `README.md` - General overview
- `WEB_INTERFACE.md` - Detailed web interface guide
- `QUICK_START.md` - Quick start guide
- `LAUNCH_GUIDE.md` - GUI launch guide
