import re

def clean_paragraph(paragraph):
    """
    Функція видаляє усі знаки пунктуації, спеціальні символи, теги та числа з абзацу тексту.

    :param paragraph: Вхідний абзац тексту
    :return: Очищений абзац тексту
    """
    # Видаляємо знаки пунктуації та спеціальні символи
    clean_text = re.sub(r'[^\w\s]', '', paragraph)
    
    # Видаляємо числа
    clean_text = re.sub(r'\d+', '', clean_text)
    
    # Видаляємо HTML теги
    clean_text = re.sub(r'<[^>]+>', '', clean_text)
    
    return clean_text

# Приклад використання функції
text = """
This is an example paragraph. It contains <strong>HTML tags</strong> and punctuation marks! It also has numbers like 123456.
"""

cleaned_text = clean_paragraph(text)
print(cleaned_text)
