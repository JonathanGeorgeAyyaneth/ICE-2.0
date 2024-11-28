from googletrans import Translator

translator = Translator()

def translate_text(text, target_language):
    try:
        # Perform the translation
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        print(f"Error: {e}")
        return None
