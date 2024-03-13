input_string = " Don't worry, it's a piece of cake, there will be no problem! Choose a job you love, and you will never have to work a day in your life!!! "
# Видалити пробіли на початку та наприкінці рядка
cleaned_string = input_string.strip()
# Зробити початок усіх слів із заголовної (великої літери)
capitalized_string = " ".join(word.capitalize() for word in cleaned_string.split())
# Підрахувати, скільки разів в рядок входить артикль “a”
count_a = cleaned_string.count('a')
# Знайти індекс першого входження артиклю “a”
index_first_a = cleaned_string.find('a')
# Замінити артикль “a” на займенник “any” тільки у другому реченні
split_sentences = cleaned_string.split('!')
second_sentence = split_sentences[1].replace(' a ', ' any ')
split_sentences[1] = second_sentence
modified_string = '!'.join(split_sentences)
# Розділити цей рядок на два за розподільником знак оклику
split_by_exclamation = cleaned_string.split('! ')
print("Видалені пробіли на початку та наприкінці рядка:", cleaned_string)
print("Початок усіх слів із заголовної (великої літери):", capitalized_string)
print("Кількість входжень артиклю 'a':", count_a)
print("Індекс першого входження артиклю 'a':", index_first_a)
print("Рядок після заміни артиклю 'a' на 'any' у другому реченні:", modified_string)
print("Розділений рядок за розподільником знак оклику:", split_by_exclamation)
