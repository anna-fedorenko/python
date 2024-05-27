def word_frequency(words_list):
    """
    Функція підраховує частоту появи кожного слова у списку слів та повертає результат у вигляді словника.

    :param words_list: Список слів
    :return: Словник з частотою появи кожного слова
    """
    word_count = {}
    
    # Підрахунок частоти появи кожного слова
    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

# Приклад використання функції
words_list = ['This', 'is', 'an', 'example', 'paragraph', 'This', 'is', 'another', 'example']
frequency_dict = word_frequency(words_list)
print(frequency_dict)
