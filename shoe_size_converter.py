#!/usr/bin/env python3
"""
Shoe Size Converter
Converts between US and EU shoe sizes with automatic gender detection
"""

import re
from typing import Tuple, Optional

# Shoe size conversion tables
# Men's shoes: EU = US + 33
MENS_SHOE_SIZES = {
    # US: EU
    6: 39,
    6.5: 39.5,
    7: 40,
    7.5: 40.5,
    8: 41,
    8.5: 41.5,
    9: 42,
    9.5: 42.5,
    10: 43,
    10.5: 43.5,
    11: 44,
    11.5: 44.5,
    12: 45,
    12.5: 45.5,
    13: 46,
    13.5: 46.5,
    14: 47,
    15: 48,
}

# Women's shoes: EU = US + 30
WOMENS_SHOE_SIZES = {
    # US: EU
    4: 34,
    4.5: 34.5,
    5: 35,
    5.5: 35.5,
    6: 36,
    6.5: 36.5,
    7: 37,
    7.5: 37.5,
    8: 38,
    8.5: 38.5,
    9: 39,
    9.5: 39.5,
    10: 40,
    10.5: 40.5,
    11: 41,
    11.5: 41.5,
    12: 42,
}

# Create reverse mappings (EU to US)
MENS_EU_TO_US = {v: k for k, v in MENS_SHOE_SIZES.items()}
WOMENS_EU_TO_US = {v: k for k, v in WOMENS_SHOE_SIZES.items()}

# Keywords for gender detection
WOMENS_KEYWORDS = [
    'women', 'woman', 'womens', "women's", 'ladies', 'lady', 'female',
    'γυναικεία', 'γυναικείο', 'γυναίκα', 'dames', 'vrouwen',
    'damen', 'femme', 'mujer', 'donna'
]

MENS_KEYWORDS = [
    'men', 'man', 'mens', "men's", 'male', 'gentleman', 'gent',
    'ανδρικά', 'ανδρικό', 'άνδρας', 'heren', 'mannen',
    'herren', 'homme', 'hombre', 'uomo'
]


class ShoeSizeConverter:
    """Convert shoe sizes between US and EU with gender detection"""

    @staticmethod
    def detect_gender(text: str) -> str:
        """
        Detect if shoes are for women or men based on text.

        Args:
            text: Product title, description, or type

        Returns:
            'women', 'men', or 'unknown'
        """
        text_lower = text.lower()

        # Check for women's keywords
        for keyword in WOMENS_KEYWORDS:
            if keyword in text_lower:
                return 'women'

        # Check for men's keywords
        for keyword in MENS_KEYWORDS:
            if keyword in text_lower:
                return 'men'

        return 'unknown'

    @staticmethod
    def detect_gender_by_size(size: float, size_system: str = 'eu') -> str:
        """
        Detect gender based on shoe size.
        Women's EU sizes typically range from 35-42
        Men's EU sizes typically range from 39-48

        Args:
            size: Shoe size number
            size_system: 'eu' or 'us'

        Returns:
            'women', 'men', or 'unknown'
        """
        if size_system == 'eu':
            if 35 <= size <= 38:
                return 'women'  # Clearly women's
            elif size >= 43:
                return 'men'  # Clearly men's
            elif 39 <= size <= 42:
                return 'unknown'  # Overlap zone
            elif size < 35:
                return 'women'  # Small sizes likely women's
        elif size_system == 'us':
            if 4 <= size <= 7:
                return 'women'  # Likely women's
            elif size >= 10:
                return 'men'  # Likely men's

        return 'unknown'

    @staticmethod
    def extract_size(text: str) -> Optional[float]:
        """
        Extract shoe size from text.

        Args:
            text: Text containing shoe size

        Returns:
            Size as float, or None if not found
        """
        # Patterns for shoe sizes
        patterns = [
            r'\b(\d+(?:\.\d+)?)\s*(?:EU|eu)\b',  # 42 EU, 42.5 EU
            r'\b(\d+(?:\.\d+)?)\s*(?:US|us)\b',  # 9 US, 9.5 US
            r'\bsize\s*(\d+(?:\.\d+)?)\b',       # size 42
            r'\b(\d+(?:\.\d+)?)\s*(?:size|Size)\b',  # 42 size
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                try:
                    return float(match.group(1))
                except ValueError:
                    continue

        return None

    @classmethod
    def us_to_eu(cls, us_size: float, gender: Optional[str] = None, context: str = "") -> Optional[float]:
        """
        Convert US shoe size to EU.

        Args:
            us_size: US shoe size
            gender: 'women', 'men', or None (will try to detect)
            context: Additional text for gender detection

        Returns:
            EU size or None if conversion not possible
        """
        # Detect gender if not provided
        if gender is None or gender == 'unknown':
            if context:
                gender = cls.detect_gender(context)
            if gender == 'unknown':
                gender = cls.detect_gender_by_size(us_size, 'us')

        # Convert based on gender
        if gender == 'women' and us_size in WOMENS_SHOE_SIZES:
            return WOMENS_SHOE_SIZES[us_size]
        elif gender == 'men' and us_size in MENS_SHOE_SIZES:
            return MENS_SHOE_SIZES[us_size]
        elif gender == 'unknown':
            # Try both, prefer women's for smaller sizes
            if us_size <= 7 and us_size in WOMENS_SHOE_SIZES:
                return WOMENS_SHOE_SIZES[us_size]
            elif us_size in MENS_SHOE_SIZES:
                return MENS_SHOE_SIZES[us_size]

        # Fallback: calculate approximate conversion
        if gender == 'women' or (gender == 'unknown' and us_size <= 7):
            return round(us_size + 30, 1)
        else:
            return round(us_size + 33, 1)

    @classmethod
    def eu_to_us(cls, eu_size: float, gender: Optional[str] = None, context: str = "") -> Optional[float]:
        """
        Convert EU shoe size to US.

        Args:
            eu_size: EU shoe size
            gender: 'women', 'men', or None (will try to detect)
            context: Additional text for gender detection

        Returns:
            US size or None if conversion not possible
        """
        # Detect gender if not provided
        if gender is None or gender == 'unknown':
            if context:
                gender = cls.detect_gender(context)
            if gender == 'unknown':
                gender = cls.detect_gender_by_size(eu_size, 'eu')

        # Convert based on gender
        if gender == 'women' and eu_size in WOMENS_EU_TO_US:
            return WOMENS_EU_TO_US[eu_size]
        elif gender == 'men' and eu_size in MENS_EU_TO_US:
            return MENS_EU_TO_US[eu_size]
        elif gender == 'unknown':
            # Try both, prefer women's for smaller sizes
            if eu_size <= 38 and eu_size in WOMENS_EU_TO_US:
                return WOMENS_EU_TO_US[eu_size]
            elif eu_size in MENS_EU_TO_US:
                return MENS_EU_TO_US[eu_size]

        # Fallback: calculate approximate conversion
        if gender == 'women' or (gender == 'unknown' and eu_size <= 38):
            return round(eu_size - 30, 1)
        else:
            return round(eu_size - 33, 1)

    @classmethod
    def convert_size_in_text(cls, text: str, conversion_type: str, context: str = "", is_size_field: bool = False) -> str:
        """
        Find and convert shoe sizes in text.

        Args:
            text: Text containing shoe size
            conversion_type: 'us_to_eu' or 'eu_to_us'
            context: Additional context for gender detection
            is_size_field: If True, treats plain numbers as shoe sizes

        Returns:
            Text with converted shoe size
        """
        if not text or pd.isna(text):
            return text

        text_str = str(text).strip()

        # Detect gender from context
        gender = cls.detect_gender(context)

        # If this is a size field and contains only a number, convert it directly
        if is_size_field:
            # Check if text is just a number (possibly with .5)
            number_pattern = r'^\s*(\d+(?:\.\d+)?)\s*$'
            match = re.match(number_pattern, text_str)

            if match:
                size_num = float(match.group(1))

                if conversion_type == 'us_to_eu':
                    # Convert US to EU
                    if 4 <= size_num <= 15:  # Valid US size range
                        eu_size = cls.us_to_eu(size_num, gender, context)
                        if eu_size:
                            # Return just the number or with EU marker
                            return str(int(eu_size) if eu_size == int(eu_size) else eu_size)
                    return text_str  # Not in valid range, keep as is

                elif conversion_type == 'eu_to_us':
                    # Convert EU to US
                    if 34 <= size_num <= 48:  # Valid EU size range
                        us_size = cls.eu_to_us(size_num, gender, context)
                        if us_size:
                            # Return just the number or with US marker
                            return str(int(us_size) if us_size == int(us_size) else us_size)
                    return text_str  # Not in valid range, keep as is

        # Patterns to find and replace (for text with US/EU markers)
        if conversion_type == 'us_to_eu':
            # Find US sizes and convert to EU
            pattern = r'\b(\d+(?:\.\d+)?)\s*(?:US|us)\b'

            def replace_func(match):
                us_size = float(match.group(1))
                eu_size = cls.us_to_eu(us_size, gender, context)
                if eu_size:
                    return f"{int(eu_size) if eu_size == int(eu_size) else eu_size} EU"
                return match.group(0)

        elif conversion_type == 'eu_to_us':
            # Find EU sizes and convert to US
            pattern = r'\b(\d+(?:\.\d+)?)\s*(?:EU|eu)\b'

            def replace_func(match):
                eu_size = float(match.group(1))
                us_size = cls.eu_to_us(eu_size, gender, context)
                if us_size:
                    return f"{int(us_size) if us_size == int(us_size) else us_size} US"
                return match.group(0)

        else:
            return text_str

        return re.sub(pattern, replace_func, text_str)


# Import pandas only if needed
try:
    import pandas as pd
except ImportError:
    pd = None


def test_converter():
    """Test the shoe size converter"""
    print("\n" + "="*60)
    print("SHOE SIZE CONVERTER - TESTS")
    print("="*60 + "\n")

    converter = ShoeSizeConverter()

    # Test gender detection
    print("Gender Detection Tests:")
    test1 = "Women's running shoes"
    test2 = "Men's casual sneakers"
    test3 = "Ανδρικά παπούτσια"
    test4 = "Γυναικεία μπότες"
    print(f"  '{test1}' → {converter.detect_gender(test1)}")
    print(f"  '{test2}' → {converter.detect_gender(test2)}")
    print(f"  '{test3}' → {converter.detect_gender(test3)}")
    print(f"  '{test4}' → {converter.detect_gender(test4)}\n")

    # Test size detection by number
    print("Size-based Gender Detection:")
    print(f"  EU 35 → {converter.detect_gender_by_size(35, 'eu')} (women's)")
    print(f"  EU 44 → {converter.detect_gender_by_size(44, 'eu')} (men's)")
    print(f"  EU 40 → {converter.detect_gender_by_size(40, 'eu')} (overlap)\n")

    # Test conversions - Women's
    print("Women's Conversions (US → EU):")
    for us in [5, 6, 7, 8, 9]:
        eu = converter.us_to_eu(us, 'women')
        print(f"  US {us} → EU {eu}")

    print("\nWomen's Conversions (EU → US):")
    for eu in [35, 36, 37, 38, 39]:
        us = converter.eu_to_us(eu, 'women')
        print(f"  EU {eu} → US {us}")

    # Test conversions - Men's
    print("\nMen's Conversions (US → EU):")
    for us in [7, 8, 9, 10, 11]:
        eu = converter.us_to_eu(us, 'men')
        print(f"  US {us} → EU {eu}")

    print("\nMen's Conversions (EU → US):")
    for eu in [40, 41, 42, 43, 44]:
        us = converter.eu_to_us(eu, 'men')
        print(f"  EU {eu} → US {us}")

    # Test text conversion
    print("\nText Conversion Tests:")
    context = "Women's running shoes"
    text1 = "Available in size 7 US"
    print(f"  Context: '{context}'")
    print(f"  Original: '{text1}'")
    print(f"  Converted: '{converter.convert_size_in_text(text1, 'us_to_eu', context)}'")

    print("\n" + "="*60)
    print("✓ All tests completed!")
    print("="*60 + "\n")


if __name__ == "__main__":
    test_converter()
