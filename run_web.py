#!/usr/bin/env python3
"""
Launcher for Shopify Translator Web Interface
"""

import sys
import os
import subprocess
import webbrowser
import time

# Check for Flask
try:
    import flask
except ImportError:
    print("ERROR: Flask is not installed!")
    print("\nTo install:")
    print("  pip install flask flask-cors")
    print("\nOr:")
    print("  pip install -r requirements_web.txt")
    sys.exit(1)

# Check for other dependencies
try:
    import pandas
    import openai
    from colorama import init
except ImportError as e:
    print(f"ERROR: Missing required module: {e}")
    print("\nPlease run: pip install -r requirements.txt")
    sys.exit(1)

if __name__ == "__main__":
    print("\n" + "="*70)
    print("🌍 Shopify Product Translator - Web Interface")
    print("="*70)
    print("\n📊 Starting web server...")
    print("🌐 Your browser will open automatically")
    print("⚡ Press Ctrl+C to stop the server")
    print("\n" + "="*70 + "\n")

    # Open browser after a short delay
    def open_browser():
        time.sleep(2)
        webbrowser.open('http://localhost:5000')

    import threading
    threading.Thread(target=open_browser).start()

    # Run the server
    os.system('python web_server.py')
