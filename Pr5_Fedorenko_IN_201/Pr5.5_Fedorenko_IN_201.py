input_string = "функції та методи роботи із рядками"

# З використанням циклу while та умовного оператору if
words = input_string.split()
reversed_words_while = []
index = len(words) - 1
while index >= 0:
    reversed_words_while.append(words[index])
    index -= 1
reversed_string_while = ' '.join(reversed_words_while)
print("З використанням циклу while та умовного оператору if:", reversed_string_while)

# З використанням методів рядків та списків (split, reverse)
words = input_string.split()
words.reverse()
reversed_string_methods = ' '.join(words)
print("З використанням методів рядків та списків (split, reverse):", reversed_string_methods)
