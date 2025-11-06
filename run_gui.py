#!/usr/bin/env python3
"""
Launcher for Shopify Translator GUI
"""

import sys
import os

# Check for tkinter
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    print("ERROR: tkinter is not installed!")
    print("\nTo install tkinter:")
    print("  Ubuntu/Debian: sudo apt-get install python3-tk")
    print("  Fedora: sudo dnf install python3-tkinter")
    print("  macOS: tkinter comes with Python")
    print("  Windows: tkinter comes with Python")
    sys.exit(1)

# Check for required modules
try:
    import pandas
    import openai
    from colorama import init
    from tqdm import tqdm
except ImportError as e:
    print(f"ERROR: Missing required module: {e}")
    print("\nPlease run: pip install -r requirements.txt")
    sys.exit(1)

# Launch GUI
from shopify_translator_gui import main

if __name__ == "__main__":
    print("🚀 Launching Shopify Translator GUI...")
    main()
