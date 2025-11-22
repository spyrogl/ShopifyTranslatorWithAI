#!/usr/bin/env python3
"""
Comprehensive Language List
Support for 100+ languages with ISO 639-1 codes
"""

# All supported languages with their native names and codes
ALL_LANGUAGES = {
    # European Languages
    'greek': {'name': 'Ελληνικά (Greek)', 'code': 'el', 'native': 'Ελληνικά'},
    'english': {'name': 'English', 'code': 'en', 'native': 'English'},
    'spanish': {'name': 'Español (Spanish)', 'code': 'es', 'native': 'Español'},
    'french': {'name': 'Français (French)', 'code': 'fr', 'native': 'Français'},
    'german': {'name': 'Deutsch (German)', 'code': 'de', 'native': 'Deutsch'},
    'italian': {'name': 'Italiano (Italian)', 'code': 'it', 'native': 'Italiano'},
    'portuguese': {'name': 'Português (Portuguese)', 'code': 'pt', 'native': 'Português'},
    'dutch': {'name': 'Nederlands (Dutch)', 'code': 'nl', 'native': 'Nederlands'},
    'russian': {'name': 'Русский (Russian)', 'code': 'ru', 'native': 'Русский'},
    'polish': {'name': 'Polski (Polish)', 'code': 'pl', 'native': 'Polski'},
    'ukrainian': {'name': 'Українська (Ukrainian)', 'code': 'uk', 'native': 'Українська'},
    'czech': {'name': 'Čeština (Czech)', 'code': 'cs', 'native': 'Čeština'},
    'romanian': {'name': 'Română (Romanian)', 'code': 'ro', 'native': 'Română'},
    'hungarian': {'name': 'Magyar (Hungarian)', 'code': 'hu', 'native': 'Magyar'},
    'swedish': {'name': 'Svenska (Swedish)', 'code': 'sv', 'native': 'Svenska'},
    'norwegian': {'name': 'Norsk (Norwegian)', 'code': 'no', 'native': 'Norsk'},
    'danish': {'name': 'Dansk (Danish)', 'code': 'da', 'native': 'Dansk'},
    'finnish': {'name': 'Suomi (Finnish)', 'code': 'fi', 'native': 'Suomi'},
    'bulgarian': {'name': 'Български (Bulgarian)', 'code': 'bg', 'native': 'Български'},
    'croatian': {'name': 'Hrvatski (Croatian)', 'code': 'hr', 'native': 'Hrvatski'},
    'serbian': {'name': 'Српски (Serbian)', 'code': 'sr', 'native': 'Српски'},
    'slovak': {'name': 'Slovenčina (Slovak)', 'code': 'sk', 'native': 'Slovenčina'},
    'slovenian': {'name': 'Slovenščina (Slovenian)', 'code': 'sl', 'native': 'Slovenščina'},
    'lithuanian': {'name': 'Lietuvių (Lithuanian)', 'code': 'lt', 'native': 'Lietuvių'},
    'latvian': {'name': 'Latviešu (Latvian)', 'code': 'lv', 'native': 'Latviešu'},
    'estonian': {'name': 'Eesti (Estonian)', 'code': 'et', 'native': 'Eesti'},
    'albanian': {'name': 'Shqip (Albanian)', 'code': 'sq', 'native': 'Shqip'},
    'macedonian': {'name': 'Македонски (Macedonian)', 'code': 'mk', 'native': 'Македонски'},
    'icelandic': {'name': 'Íslenska (Icelandic)', 'code': 'is', 'native': 'Íslenska'},
    'irish': {'name': 'Gaeilge (Irish)', 'code': 'ga', 'native': 'Gaeilge'},
    'welsh': {'name': 'Cymraeg (Welsh)', 'code': 'cy', 'native': 'Cymraeg'},
    'basque': {'name': 'Euskara (Basque)', 'code': 'eu', 'native': 'Euskara'},
    'catalan': {'name': 'Català (Catalan)', 'code': 'ca', 'native': 'Català'},
    'galician': {'name': 'Galego (Galician)', 'code': 'gl', 'native': 'Galego'},
    'maltese': {'name': 'Malti (Maltese)', 'code': 'mt', 'native': 'Malti'},

    # Asian Languages
    'chinese_simplified': {'name': '简体中文 (Chinese Simplified)', 'code': 'zh-CN', 'native': '简体中文'},
    'chinese_traditional': {'name': '繁體中文 (Chinese Traditional)', 'code': 'zh-TW', 'native': '繁體中文'},
    'japanese': {'name': '日本語 (Japanese)', 'code': 'ja', 'native': '日本語'},
    'korean': {'name': '한국어 (Korean)', 'code': 'ko', 'native': '한국어'},
    'arabic': {'name': 'العربية (Arabic)', 'code': 'ar', 'native': 'العربية'},
    'hebrew': {'name': 'עברית (Hebrew)', 'code': 'he', 'native': 'עברית'},
    'turkish': {'name': 'Türkçe (Turkish)', 'code': 'tr', 'native': 'Türkçe'},
    'persian': {'name': 'فارسی (Persian)', 'code': 'fa', 'native': 'فارسی'},
    'urdu': {'name': 'اردو (Urdu)', 'code': 'ur', 'native': 'اردو'},
    'hindi': {'name': 'हिन्दी (Hindi)', 'code': 'hi', 'native': 'हिन्दी'},
    'bengali': {'name': 'বাংলা (Bengali)', 'code': 'bn', 'native': 'বাংলা'},
    'punjabi': {'name': 'ਪੰਜਾਬੀ (Punjabi)', 'code': 'pa', 'native': 'ਪੰਜਾਬੀ'},
    'tamil': {'name': 'தமிழ் (Tamil)', 'code': 'ta', 'native': 'தமிழ்'},
    'telugu': {'name': 'తెలుగు (Telugu)', 'code': 'te', 'native': 'తెలుగు'},
    'marathi': {'name': 'मराठी (Marathi)', 'code': 'mr', 'native': 'मराठी'},
    'gujarati': {'name': 'ગુજરાતી (Gujarati)', 'code': 'gu', 'native': 'ગુજરાતી'},
    'kannada': {'name': 'ಕನ್ನಡ (Kannada)', 'code': 'kn', 'native': 'ಕನ್ನಡ'},
    'malayalam': {'name': 'മലയാളം (Malayalam)', 'code': 'ml', 'native': 'മലയാളം'},
    'thai': {'name': 'ไทย (Thai)', 'code': 'th', 'native': 'ไทย'},
    'vietnamese': {'name': 'Tiếng Việt (Vietnamese)', 'code': 'vi', 'native': 'Tiếng Việt'},
    'indonesian': {'name': 'Bahasa Indonesia (Indonesian)', 'code': 'id', 'native': 'Bahasa Indonesia'},
    'malay': {'name': 'Bahasa Melayu (Malay)', 'code': 'ms', 'native': 'Bahasa Melayu'},
    'filipino': {'name': 'Filipino (Tagalog)', 'code': 'fil', 'native': 'Filipino'},
    'burmese': {'name': 'မြန်မာဘာသာ (Burmese)', 'code': 'my', 'native': 'မြန်မာဘာသာ'},
    'khmer': {'name': 'ខ្មែរ (Khmer)', 'code': 'km', 'native': 'ខ្មែរ'},
    'lao': {'name': 'ລາວ (Lao)', 'code': 'lo', 'native': 'ລາວ'},
    'sinhala': {'name': 'සිංහල (Sinhala)', 'code': 'si', 'native': 'සිංහල'},
    'nepali': {'name': 'नेपाली (Nepali)', 'code': 'ne', 'native': 'नेपाली'},
    'mongolian': {'name': 'Монгол (Mongolian)', 'code': 'mn', 'native': 'Монгол'},
    'georgian': {'name': 'ქართული (Georgian)', 'code': 'ka', 'native': 'ქართული'},
    'armenian': {'name': 'Հայերեն (Armenian)', 'code': 'hy', 'native': 'Հայերեն'},
    'azerbaijani': {'name': 'Azərbaycan (Azerbaijani)', 'code': 'az', 'native': 'Azərbaycan'},
    'kazakh': {'name': 'Қазақ (Kazakh)', 'code': 'kk', 'native': 'Қазақ'},
    'uzbek': {'name': 'Oʻzbek (Uzbek)', 'code': 'uz', 'native': 'Oʻzbek'},

    # African Languages
    'swahili': {'name': 'Kiswahili (Swahili)', 'code': 'sw', 'native': 'Kiswahili'},
    'afrikaans': {'name': 'Afrikaans', 'code': 'af', 'native': 'Afrikaans'},
    'amharic': {'name': 'አማርኛ (Amharic)', 'code': 'am', 'native': 'አማርኛ'},
    'yoruba': {'name': 'Yorùbá', 'code': 'yo', 'native': 'Yorùbá'},
    'igbo': {'name': 'Igbo', 'code': 'ig', 'native': 'Igbo'},
    'zulu': {'name': 'isiZulu (Zulu)', 'code': 'zu', 'native': 'isiZulu'},
    'xhosa': {'name': 'isiXhosa (Xhosa)', 'code': 'xh', 'native': 'isiXhosa'},
    'hausa': {'name': 'Hausa', 'code': 'ha', 'native': 'Hausa'},
    'somali': {'name': 'Soomaali (Somali)', 'code': 'so', 'native': 'Soomaali'},

    # American Languages
    'chilean': {'name': 'Español Chileno (Chilean Spanish)', 'code': 'es-CL', 'native': 'Español Chileno'},
    'mexican': {'name': 'Español Mexicano (Mexican Spanish)', 'code': 'es-MX', 'native': 'Español Mexicano'},
    'argentinian': {'name': 'Español Argentino (Argentinian Spanish)', 'code': 'es-AR', 'native': 'Español Argentino'},
    'colombian': {'name': 'Español Colombiano (Colombian Spanish)', 'code': 'es-CO', 'native': 'Español Colombiano'},
    'brazilian': {'name': 'Português Brasileiro (Brazilian Portuguese)', 'code': 'pt-BR', 'native': 'Português Brasileiro'},
    'quebecois': {'name': 'Français Québécois (Quebec French)', 'code': 'fr-CA', 'native': 'Français Québécois'},

    # Oceanic Languages
    'maori': {'name': 'Te Reo Māori (Maori)', 'code': 'mi', 'native': 'Te Reo Māori'},
    'samoan': {'name': 'Gagana Samoa (Samoan)', 'code': 'sm', 'native': 'Gagana Samoa'},
    'hawaiian': {'name': 'ʻŌlelo Hawaiʻi (Hawaiian)', 'code': 'haw', 'native': 'ʻŌlelo Hawaiʻi'},

    # Additional Languages
    'esperanto': {'name': 'Esperanto', 'code': 'eo', 'native': 'Esperanto'},
    'latin': {'name': 'Latina (Latin)', 'code': 'la', 'native': 'Latina'},
}


def get_simple_translation_prompt() -> str:
    """
    Returns a simple translation prompt for field-by-field translation.
    This is used by translate_text() for individual fields.

    Returns:
        Simple translation prompt
    """
    return """You are a professional e-commerce translator.

You will receive a CONFIG section with parameters and a TEXT TO TRANSLATE.

RULES:

1. AUTO-DETECT the source language (could be Estonian, Greek, English, Spanish, etc.)

2. Translate to the target_language specified in CONFIG

3. PRESERVE:
   - S, M, L, XL, XXL clothing sizes (never translate)
   - Numeric clothing sizes: 34, 36, 38, etc.
   - HTML tags: <p>, <ul>, <li>, <b>, <i>, <br>
   - Emojis, bullet points, formatting
   - Image URLs (anything with .jpg, .png, .webp, http)

4. TRANSLATE:
   - Product titles, descriptions, features
   - Color names
   - Option names like "Suurus" → "Size" equivalent in target language
   - Marketing copy

5. DO NOT:
   - Mention countries, cities, locations
   - Translate technical codes (SKU, barcode, etc.)
   - Add explanations or notes

6. OUTPUT:
   - Return ONLY the translated text
   - No markdown, no explanations
   - Keep the same structure and formatting

7. TITLE LENGTH LIMIT (CRITICAL):
   - If field_type is Title, the translation MUST be LESS THAN 250 characters
   - Keep titles concise and impactful
   - Remove unnecessary words if needed to stay under 250 characters
   - NEVER exceed 250 characters for titles

Example CONFIG usage:
- If CONFIG says target_language: es, translate "Suurus" → "Talla"
- If CONFIG says target_language: fr, translate "Suurus" → "Taille"
- If CONFIG says target_language: el, translate "Suurus" → "Μέγεθος"

For Body (HTML) fields:
- Structure with 1 short paragraph + exactly 4 bullet points
- Use <p> and <ul><li> tags

Return ONLY the translated text."""


# ΤΕΛΙΚΟ – ΕΝΙΑΙΟ SYSTEM PROMPT (for full CSV processing)
def get_unified_system_prompt() -> str:
    """
    Returns the FINAL UNIFIED SYSTEM PROMPT exactly as specified.
    This prompt expects CONFIG + CSV in the user message.

    Returns:
        Complete system prompt for CSV translation
    """
    return """📌 SYSTEM PROMPT – Shopify CSV Translator & Shoe Size Converter

You are a strict Shopify CSV translation and product-processing engine.
You will always receive one message from the user containing:

a CONFIG section (plain text parameters)

a CSV section (the full Shopify CSV file)

You MUST always:

read the CONFIG section

apply its parameters exactly

process the CSV using the rules below

output ONLY the final processed CSV

keep the CSV structure 100% identical:

same rows

same columns

same order

same delimiter

same quoting

No explanations. No descriptions. No Markdown.

1. SOURCE LANGUAGE

The product text may be in ANY language (Estonian, Greek, Spanish, French, etc.).
You MUST:

auto-detect the source language

translate ALL required text fields into target_language from CONFIG

2. FIELDS TO TRANSLATE

Translate only:

Title

Body (HTML)

SEO Title

SEO Description

Tags (text tags only)

Color names (Option1 Value when it is a color)

Option Names such as "Size", "Suurus", "Värv", "Color", etc.
→ Translate to the target-language equivalent.
Example: Size → Talla (ES), Taille (FR), Größe (DE)

Do NOT translate Option Values if they are sizes.

3. DO-NOT-TOUCH FIELDS

You MUST NOT modify or translate:

Handle

Vendor

Product Category

Type

Variant SKU

Variant Price

Variant Compare At Price

Variant Barcode

Variant Grams

Gift Card

Inventory fields

Fulfillment fields

Unit Price fields

Status

ANY numeric-only field that is NOT a shoe size

ANY technical field

4. IMAGE FIELDS — NEVER MODIFY

Never change or translate:

Image Src

Variant Image

Image Alt Text if it is a URL

any value containing:

.jpg, .jpeg, .png, .webp

http:// or https://

You must copy these fields exactly as they are.

5. CLOTHING SIZE RULES

If the product is NOT shoes:

Translate option name "Suurus" (or any "Size" equivalent)

Do NOT change size values:

S, M, L, XL, XXL

numeric clothing sizes (34, 36, 38…)

Keep them exactly the same.

6. SHOE DETECTION

Classify the product as shoes if Title, Tags, or Body contains words like:

English: shoes, boots, sneakers, heels

Estonian: saabast, saapad, kingad, kontsad, jalanõud

Greek: παπούτσια, μπότες, γόβες

Spanish: zapatos, botas, tacones

etc.

If no shoe keywords → clothing → no conversion.

7. GENDER DETECTION

Determine gender using Title, Tags, Body:

Women keywords:

women, female, ladies, naiste, naistele, mujer, femme, Γυναικεία

Men keywords:

meeste, meestele, men, masculino, homme, Ανδρικά

If both appear → unisex
If none appear → use default_shoe_gender from CONFIG
If still unclear → DO NOT convert sizes.

8. SHOE SIZE CONVERSION

Convert ONLY if:

the product is shoes
AND

convert_shoe_sizes is NOT "NONE"
AND

gender is determined

Convert ONLY the shoe numeric values found in Option2 Value.
Return ONLY the number (no "EU", "US", "Size", etc.).

Use the conversion tables from CONFIG (EU_TO_US and US_TO_EQ for men and women).

If a size is missing from the table → leave it unchanged.

9. CSV OUTPUT

You MUST:

keep the CSV exactly the same structure

output ONLY the final CSV

no commentary, no markdown, no explanations

END OF SYSTEM PROMPT"""


def get_conversion_tables() -> str:
    """
    Returns the exact shoe size conversion tables as text.

    Returns:
        Conversion tables in text format for CONFIG
    """
    return """
EU_TO_US_WOMEN:
35 → 4
36 → 5
37 → 6
37.5 → 6.5
38 → 7
39 → 8
40 → 9
41 → 10
42 → 11

US_TO_EU_WOMEN:
4 → 35
5 → 36
6 → 37
6.5 → 37.5
7 → 38
8 → 39
9 → 40
10 → 41
11 → 42

EU_TO_US_MEN:
39 → 6
40 → 7
41 → 8
42 → 9
43 → 10
44 → 11
45 → 12
46 → 13

US_TO_EU_MEN:
6 → 39
7 → 40
8 → 41
9 → 42
10 → 43
11 → 44
12 → 45
13 → 46"""


def build_config_section(target_language: str, convert_shoe_sizes: str = "NONE", default_shoe_gender: str = "women") -> str:
    """
    Builds the CONFIG section for the user message.

    Args:
        target_language: Target language code (e.g., "el", "es", "fr")
        convert_shoe_sizes: "NONE", "EU_TO_US", or "US_TO_EU"
        default_shoe_gender: "women", "men", or "unisex"

    Returns:
        CONFIG section as string
    """
    config = f"""CONFIG
target_language: {target_language}
convert_shoe_sizes: {convert_shoe_sizes}
default_shoe_gender: {default_shoe_gender}"""

    # Add conversion tables if needed
    if convert_shoe_sizes != "NONE":
        config += "\n" + get_conversion_tables()

    return config


# Legacy function for backward compatibility (now calls unified prompt)
def get_translation_prompt(language_name: str, language_code: str, mode: str = 'market_adaptation') -> str:
    """
    Legacy function - returns unified system prompt.
    Kept for backward compatibility.

    Args:
        language_name: Full name of the language (e.g., "Español (Spanish)")
        language_code: ISO language code (e.g., "es")
        mode: 'market_adaptation' or 'direct'

    Returns:
        System prompt for translation
    """
    return get_unified_system_prompt()


# Standard option names for consistent branding (extended list)
STANDARD_OPTION_NAMES_EXTENDED = {
    'greek': {
        'color': 'Χρώμα', 'colour': 'Χρώμα',
        'size': 'Μέγεθος', 'material': 'Υλικό',
        'style': 'Στυλ', 'pattern': 'Μοτίβο',
        'finish': 'Φινίρισμα', 'type': 'Τύπος',
        'length': 'Μήκος', 'width': 'Πλάτος',
        'weight': 'Βάρος', 'fit': 'Εφαρμογή',
    },
    'spanish': {
        'color': 'Color', 'colour': 'Color',
        'size': 'Talla', 'material': 'Material',
        'style': 'Estilo', 'pattern': 'Patrón',
        'finish': 'Acabado', 'type': 'Tipo',
        'length': 'Largo', 'width': 'Ancho',
        'weight': 'Peso', 'fit': 'Ajuste',
    },
    'french': {
        'color': 'Couleur', 'colour': 'Couleur',
        'size': 'Taille', 'material': 'Matériau',
        'style': 'Style', 'pattern': 'Motif',
        'finish': 'Finition', 'type': 'Type',
        'length': 'Longueur', 'width': 'Largeur',
        'weight': 'Poids', 'fit': 'Coupe',
    },
    'german': {
        'color': 'Farbe', 'colour': 'Farbe',
        'size': 'Größe', 'material': 'Material',
        'style': 'Stil', 'pattern': 'Muster',
        'finish': 'Oberfläche', 'type': 'Typ',
        'length': 'Länge', 'width': 'Breite',
        'weight': 'Gewicht', 'fit': 'Passform',
    },
    'italian': {
        'color': 'Colore', 'colour': 'Colore',
        'size': 'Taglia', 'material': 'Materiale',
        'style': 'Stile', 'pattern': 'Motivo',
        'finish': 'Finitura', 'type': 'Tipo',
        'length': 'Lunghezza', 'width': 'Larghezza',
        'weight': 'Peso', 'fit': 'Vestibilità',
    },
    'portuguese': {
        'color': 'Cor', 'colour': 'Cor',
        'size': 'Tamanho', 'material': 'Material',
        'style': 'Estilo', 'pattern': 'Padrão',
        'finish': 'Acabamento', 'type': 'Tipo',
        'length': 'Comprimento', 'width': 'Largura',
        'weight': 'Peso', 'fit': 'Ajuste',
    },
    'dutch': {
        'color': 'Kleur', 'colour': 'Kleur',
        'size': 'Maat', 'material': 'Materiaal',
        'style': 'Stijl', 'pattern': 'Patroon',
        'finish': 'Afwerking', 'type': 'Type',
        'length': 'Lengte', 'width': 'Breedte',
        'weight': 'Gewicht', 'fit': 'Pasvorm',
    },
}
