"""
deep_translator: python library to translate
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    function to translate Englist to french
    """
    french_text = MyMemoryTranslator(source="english", target="french").translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    function to translate french to english
    """
    english_text = MyMemoryTranslator(source="french", target="english").translate(french_text)
    return english_text
