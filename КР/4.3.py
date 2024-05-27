def split_into_words(paragraph):
    """
    Функція розбиває абзац тексту на окремі слова за роздільником пробілу.

    :param paragraph: Вхідний абзац тексту
    :return: Список слів
    """
    # Розбиваємо абзац тексту на слова за роздільником пробілу
    words = paragraph.split()
    
    return words

# Приклад використання функції
text = "This is an example paragraph. It contains <strong>HTML tags</strong> and punctuation marks! It also has numbers like 123456."
words_list = split_into_words(text)
print(words_list)
