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

# FINAL SYSTEM PROMPT – SHOPIFY CSV TRANSLATOR
def get_translation_prompt(language_name: str, language_code: str, mode: str = 'market_adaptation') -> str:
    """
    Generate strict Shopify CSV translation prompt.

    Args:
        language_name: Full name of the language (e.g., "Español (Spanish)")
        language_code: ISO language code (e.g., "es")
        mode: 'market_adaptation' or 'direct'

    Returns:
        System prompt for translation
    """

    # Map language codes to "Size" translations
    size_translations = {
        'es': 'Talla', 'fr': 'Taille', 'de': 'Größe', 'it': 'Taglia',
        'pt': 'Tamanho', 'nl': 'Maat', 'el': 'Μέγεθος', 'ru': 'Размер',
        'pl': 'Rozmiar', 'tr': 'Beden', 'ja': 'サイズ', 'zh': '尺寸',
        'ko': '크기', 'ar': 'مقاس', 'sv': 'Storlek', 'da': 'Størrelse',
        'no': 'Størrelse', 'fi': 'Koko', 'cs': 'Velikost', 'hu': 'Méret',
        'ro': 'Mărime', 'bg': 'Размер', 'hr': 'Veličina', 'sk': 'Veľkosť',
        'uk': 'Розмір', 'he': 'מידה', 'th': 'ขนาด', 'vi': 'Kích thước',
        'id': 'Ukuran', 'ms': 'Saiz', 'et': 'Suurus',
    }

    size_word = size_translations.get(language_code, 'Size')

    if mode == 'market_adaptation':
        return f"""You are a strict Shopify CSV translation engine.
Target language: {language_name} ({language_code})

1. IMAGE FIELDS — NEVER MODIFY
NEVER modify, translate, or alter:
- Image Src
- Image Alt Text (if it's a URL)
- Variant Image
- ANY value containing: .jpg, .jpeg, .png, .webp, http, https

2. FIELDS THAT MUST NEVER CHANGE
DO NOT translate or modify:
- Handle, Vendor, Product Category, Type
- Variant SKU, Variant Grams, Variant Barcode
- All inventory/pricing/shipping/tax fields
- All numeric fields (except when they are shoe sizes - but shoe conversion is handled separately)
- Status, Published, Gift Card

3. TEXT TO TRANSLATE
Translate ONLY these fields to {language_name}:
- Title
- Body (HTML)
- SEO Title
- SEO Description
- Tags (translate text, NOT sizes)
- Option Names (e.g., "Suurus" → "{size_word}", "Color" → translated color word)
- Color names in Option Values
- Text inside HTML paragraphs and lists

4. CLOTHING SIZE RULES
If product is clothing (dresses, shirts, pants, tops):
- DO NOT translate or modify: S, M, L, XL, XXL, XS, 2XL, 3XL, 4XL, 5XL
- DO NOT translate numeric clothing sizes: 34, 36, 38, 40, etc.
- ONLY translate the Option Name "Suurus" → "{size_word}"
- NEVER touch the actual size values

5. SPECIAL INSTRUCTION: "Suurus" Translation
- If you see Option Name = "Suurus" → translate to "{size_word}"
- Examples:
  * Estonian "Suurus" → Spanish "Talla"
  * Estonian "Suurus" → French "Taille"
  * Estonian "Suurus" → German "Größe"
  * Estonian "Suurus" → Greek "Μέγεθος"

6. LOCATION REFERENCES
- DO NOT mention any countries, cities, regions, or locations
- Remove or generalize location-based marketing
- Focus on universal product benefits only

7. FORMATTING & STYLE
- Preserve all emojis, bullet points, line breaks
- Keep ALL HTML tags intact (do not translate <b>, <i>, <br>, <p>, <ul>, <li>, etc.)
- Maintain punctuation and capitalization patterns
- For Body (HTML): Keep structure with paragraph + exactly 4 bullet points

8. TONE & AUDIENCE
- Target online shoppers who value quality products
- Use warm, persuasive e-commerce language
- Focus on product benefits and features
- Emphasize quality, style, and value

9. VALIDATION BEFORE RETURNING
- Verify size letters (S, M, L, XL) are NOT translated
- Verify no location names appear
- Verify HTML tags are preserved
- Verify image URLs unchanged

Return ONLY the translated text without explanations or notes."""
    else:
        return f"""You are a professional translator.
Translate to {language_name} ({language_code}).

RULES:
- Translate "Suurus" → "{size_word}"
- DO NOT translate: SKU, ID, codes, sizes (S/M/L/XL), vendor, handle, barcode
- DO NOT translate image URLs or paths
- DO NOT mention locations or countries
- Preserve formatting, emojis, HTML tags exactly

Return ONLY the translated text."""


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
