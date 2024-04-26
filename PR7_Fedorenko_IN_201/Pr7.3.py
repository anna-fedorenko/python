def filter_words_starting_with_letter(string_1):
    letter = input("Введіть букву: ")
    return list(filter(lambda word: word.startswith(letter), string_1.split()))

def filter_words_containing_letter(string_1):
    letter = input("Введіть букву: ")
    return list(filter(lambda word: letter in word, string_1.split()))

def filter_words_by_length(string_1, length):
    return list(filter(lambda word: len(word) == length, string_1.split()))

def reverse_words(string_1):
    return string_1.split()[::-1]

def filter_words_starting_with_prefix(string_1, prefix):
    return list(filter(lambda word: word.startswith(prefix), string_1.split()))

# Приклад використання:

string_1 = "apple banana orange pear pineapple yellow red green brown town purple sun gurden juice"

print("Слова, які починаються з заданої букви:")
print(filter_words_starting_with_letter(string_1))

print("\nСлова, які містять задану букву:")
print(filter_words_containing_letter(string_1))

print("\nСлова заданої довжини:")
print(filter_words_by_length(string_1, 6))

print("\nСлова в зворотному порядку:")
print(reverse_words(string_1))

print("\nСлова, які починаються з заданого префіксу:")
prefix = input("Введіть префікс: ")
print(filter_words_starting_with_prefix(string_1, prefix))
