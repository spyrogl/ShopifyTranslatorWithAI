#!/usr/bin/env python3
"""
Shopify Translator - Web Server
Flask-based web interface for the Shopify Product Translator
"""

import os
import json
import sys
from pathlib import Path
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file, send_from_directory
from werkzeug.utils import secure_filename

# Import the translator
from shopify_translator import ShopifyTranslator, MARKET_ADAPTATIONS, TRANSLATABLE_FIELDS
from languages import ALL_LANGUAGES

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'translated_outputs'

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
os.makedirs('backups', exist_ok=True)

# Store active translation sessions
translation_sessions = {}


@app.route('/')
def index():
    """Serve the main HTML interface"""
    return send_from_directory('.', 'web_interface.html')


@app.route('/api/languages', methods=['GET'])
def get_languages():
    """Get available languages - all 100+ languages sorted alphabetically"""
    languages = []
    for key, lang in ALL_LANGUAGES.items():
        languages.append({
            'key': key,
            'name': lang['name'],
            'code': lang['code'],
            'native': lang.get('native', lang['name'])
        })
    # Sort alphabetically by name
    languages.sort(key=lambda x: x['name'])
    return jsonify({'languages': languages})


@app.route('/api/fields', methods=['GET'])
def get_fields():
    """Get translatable fields"""
    return jsonify({'fields': TRANSLATABLE_FIELDS})


@app.route('/api/upload', methods=['POST'])
def upload_file():
    """Handle CSV file upload"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not file.filename.endswith('.csv'):
        return jsonify({'error': 'File must be a CSV'}), 400

    # Save file
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Analyze file
    try:
        import pandas as pd
        df = pd.read_csv(filepath, encoding='utf-8')

        analysis = {
            'filename': filename,
            'filepath': filepath,
            'total_rows': len(df),
            'unique_products': df['Handle'].nunique() if 'Handle' in df.columns else 0,
            'columns': list(df.columns),
            'available_fields': [f for f in TRANSLATABLE_FIELDS if f in df.columns]
        }

        return jsonify(analysis)
    except Exception as e:
        return jsonify({'error': f'Error analyzing file: {str(e)}'}), 400


@app.route('/api/estimate', methods=['POST'])
def estimate_cost():
    """Estimate translation cost"""
    data = request.json

    try:
        products = data.get('products', 0)
        fields = len(data.get('fields', []))
        model = data.get('model', 'gpt-4o-mini')

        # Rough estimation
        tokens_per_field = 100
        total_tokens = products * fields * tokens_per_field

        if model == 'gpt-4o-mini':
            cost_per_1k = 0.00015
            cost_per_product = 0.001
        else:
            cost_per_1k = 0.0025
            cost_per_product = 0.013

        estimated_cost_min = (total_tokens / 1000) * cost_per_1k
        estimated_cost_max = estimated_cost_min * 2

        return jsonify({
            'products': products,
            'fields': fields,
            'estimated_tokens': total_tokens,
            'cost_min': round(estimated_cost_min, 3),
            'cost_max': round(estimated_cost_max, 3),
            'cost_per_product': cost_per_product
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/translate', methods=['POST'])
def start_translation():
    """Start translation process"""
    data = request.json

    try:
        # Get parameters
        filepath = data.get('filepath')
        api_key = data.get('api_key')
        target_language = data.get('target_language')
        translation_mode = data.get('translation_mode', 'market_adaptation')
        model = data.get('model', 'gpt-4o-mini')
        fields = data.get('fields', [])
        special_instructions = data.get('special_instructions', '')
        shoe_conversion = data.get('shoe_conversion', 'none')
        default_gender = data.get('default_gender', 'women')

        if not all([filepath, api_key, target_language, fields]):
            return jsonify({'error': 'Missing required parameters'}), 400

        # Save API key to config
        config = {'openai_api_key': api_key}
        with open('config.json', 'w') as f:
            json.dump(config, f)

        # Create session ID
        session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Store session info
        translation_sessions[session_id] = {
            'status': 'starting',
            'progress': 0,
            'message': 'Initializing...'
        }

        # Start translation in background
        import threading
        thread = threading.Thread(
            target=run_translation,
            args=(session_id, filepath, target_language, translation_mode, model, fields, special_instructions, shoe_conversion, default_gender)
        )
        thread.daemon = True
        thread.start()

        return jsonify({
            'session_id': session_id,
            'status': 'started'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/progress/<session_id>', methods=['GET'])
def get_progress(session_id):
    """Get translation progress"""
    if session_id not in translation_sessions:
        return jsonify({'error': 'Session not found'}), 404

    return jsonify(translation_sessions[session_id])


@app.route('/api/download/<filename>', methods=['GET'])
def download_file(filename):
    """Download translated file"""
    try:
        filepath = os.path.join(app.config['OUTPUT_FOLDER'], filename)
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 404


def run_translation(session_id, filepath, target_language, translation_mode, model, fields, special_instructions, shoe_conversion, default_gender='women'):
    """Run translation in background"""
    try:
        # Update status
        translation_sessions[session_id]['status'] = 'translating'
        translation_sessions[session_id]['message'] = 'Loading translator...'

        # Create translator
        translator = ShopifyTranslator()

        # Load file
        translation_sessions[session_id]['message'] = 'Loading CSV file...'
        import pandas as pd
        translator.df = pd.read_csv(filepath, encoding='utf-8')

        # Create backup
        translation_sessions[session_id]['message'] = 'Creating backup...'
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"backup_{timestamp}_{os.path.basename(filepath)}"
        translator.backup_path = os.path.join('backups', backup_filename)
        translator.df.to_csv(translator.backup_path, index=False, encoding='utf-8')

        # Setup API client
        translation_sessions[session_id]['message'] = 'Connecting to OpenAI...'
        from openai import OpenAI
        translator.client = OpenAI(api_key=json.load(open('config.json'))['openai_api_key'])

        # Prepare settings
        settings = {
            'target_language': target_language,
            'translation_mode': translation_mode,
            'model': model,
            'special_instructions': special_instructions
        }

        # Load cache
        translator.cache = translator.load_cache()

        # Get unique products
        unique_handles = translator.df['Handle'].unique()
        total_products = len(unique_handles)

        translation_sessions[session_id]['message'] = f'Translating {total_products} products...'
        translation_sessions[session_id]['total'] = total_products

        # Translate each product
        for i, handle in enumerate(unique_handles):
            product_rows = translator.df[translator.df['Handle'] == handle]
            first_row_idx = product_rows.index[0]

            # Update progress
            progress = int((i / total_products) * 100)
            translation_sessions[session_id]['progress'] = progress
            translation_sessions[session_id]['message'] = f'Translating product {i+1}/{total_products}...'

            # Translate fields
            for field in fields:
                if field not in translator.df.columns:
                    continue

                # Handle variants
                if field in ['Option1 Name', 'Option2 Name', 'Option3 Name',
                           'Option1 Value', 'Option2 Value', 'Option3 Value']:
                    unique_values = product_rows[field].dropna().unique()
                    for unique_val in unique_values:
                        if unique_val and str(unique_val).strip():
                            translated_val = translator.translate_text(str(unique_val), settings, field)
                            mask = (translator.df['Handle'] == handle) & (translator.df[field] == unique_val)
                            translator.df.loc[mask, field] = translated_val
                else:
                    # Non-variant fields
                    value = translator.df.at[first_row_idx, field]
                    if pd.notna(value) and value != "":
                        translated = translator.translate_text(str(value), settings, field)
                        translator.df.at[first_row_idx, field] = translated

            # Save cache periodically
            if i % 10 == 0:
                translator.save_cache()

        # Final cache save
        translator.save_cache()

        # Apply shoe size conversion if requested
        if shoe_conversion != 'none':
            translation_sessions[session_id]['message'] = 'Converting shoe sizes...'
            from shoe_size_converter import ShoeSizeConverter

            # Size keywords in various languages
            size_keywords = ['size', 'μέγεθος', 'talla', 'maat', 'größe', 'taille', 'taglia', 'tamanho', 'suurus']

            for idx, row in translator.df.iterrows():
                # Get context for gender and shoe detection
                context = ""
                tags = ""
                if 'Title' in translator.df.columns:
                    context += str(row.get('Title', '')) + " "
                if 'Type' in translator.df.columns:
                    context += str(row.get('Type', '')) + " "
                if 'Tags' in translator.df.columns:
                    tags = str(row.get('Tags', ''))
                if 'Body (HTML)' in translator.df.columns:
                    context += str(row.get('Body (HTML)', ''))[:200]  # First 200 chars

                # Check if this product is shoes (according to SYSTEM PROMPT rules)
                is_shoe_product = ShoeSizeConverter.is_shoe_product(context, tags)

                # Only convert if it's a shoe product
                if not is_shoe_product:
                    continue

                # Detect gender (or use default if cannot detect)
                detected_gender = ShoeSizeConverter.detect_gender(context)
                if detected_gender == 'unknown':
                    detected_gender = default_gender  # Use default from user selection

                # Check each Option field
                for i in [1, 2, 3]:
                    name_field = f'Option{i} Name'
                    value_field = f'Option{i} Value'

                    # Check if this option is for shoe sizes
                    is_size_field = False
                    if name_field in translator.df.columns:
                        option_name = str(row.get(name_field, '')).lower()
                        is_size_field = any(keyword in option_name for keyword in size_keywords)

                    # Convert the value if it's a size field
                    if is_size_field and value_field in translator.df.columns:
                        value = row.get(value_field)
                        if pd.notna(value) and value != "":
                            # Convert based on direction with detected gender
                            try:
                                value_num = float(str(value).strip())
                                converted_num = None

                                if shoe_conversion == 'us_to_eu':
                                    converted_num = ShoeSizeConverter.us_to_eu(value_num, detected_gender, context)
                                elif shoe_conversion == 'eu_to_us':
                                    converted_num = ShoeSizeConverter.eu_to_us(value_num, detected_gender, context)

                                # Return only numeric size (no "EU", "US", "size")
                                if converted_num:
                                    converted = str(int(converted_num) if converted_num == int(converted_num) else converted_num)
                                    translator.df.at[idx, value_field] = converted
                            except (ValueError, TypeError):
                                # If not a number, keep as is
                                pass

        # Save output
        translation_sessions[session_id]['message'] = 'Saving output...'

        # Generate new filename format: TranslatedWithAI{count}{DDMMYYYY}{HHMM}
        now = datetime.now()
        product_count = len(unique_handles)
        date_str = now.strftime('%d%m%Y')  # DDMMYYYY
        time_str = now.strftime('%H%M')     # HHMM
        output_filename = f"TranslatedWithAI{product_count}{date_str}{time_str}.csv"

        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
        translator.df.to_csv(output_path, index=False, encoding='utf-8')

        # Get preview data (first 10 rows) and replace NaN with empty strings for JSON compatibility
        preview_df = translator.df.head(10).fillna('')
        preview_data = preview_df.to_dict('records')

        # Calculate cost
        if model == 'gpt-4o-mini':
            cost_per_1k = 0.00015
        else:
            cost_per_1k = 0.0025

        total_cost = (translator.total_tokens / 1000) * cost_per_1k * 2

        # Update final status
        translation_sessions[session_id]['status'] = 'completed'
        translation_sessions[session_id]['progress'] = 100
        translation_sessions[session_id]['message'] = 'Translation completed!'
        translation_sessions[session_id]['output_file'] = output_filename
        translation_sessions[session_id]['total_tokens'] = translator.total_tokens
        translation_sessions[session_id]['total_cost'] = round(total_cost, 3)
        translation_sessions[session_id]['product_count'] = product_count
        translation_sessions[session_id]['preview_data'] = preview_data

    except Exception as e:
        translation_sessions[session_id]['status'] = 'error'
        translation_sessions[session_id]['message'] = f'Error: {str(e)}'
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🌍 Shopify Product Translator - Web Interface")
    print("="*60)
    print("\n📊 Server starting...")
    print("🌐 Open your browser and go to: http://localhost:5000")
    print("⚡ Press Ctrl+C to stop the server")
    print("\n" + "="*60 + "\n")

    app.run(debug=True, host='0.0.0.0', port=5000)
