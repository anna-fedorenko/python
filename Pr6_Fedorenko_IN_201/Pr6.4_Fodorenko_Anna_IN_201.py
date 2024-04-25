# Дані словники
a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# Спільні пари "ключ-значення" для обох словників
common_pairs = {key: (a[key], b[key]) for key in a if key in b}
print("Спільні пари «ключ-значення»:")
for key, (value_a, value_b) in common_pairs.items():
    print(f"{key}: ({value_a}, {value_b})")

# Ключі, які присутні в першому словнику, але яких немає в другому
keys_only_in_a = [key for key in a if key not in b]
print("Ключі, які присутні в першому словнику, але яких немає в другому:")
print(' '.join(keys_only_in_a))

# Об'єднання двох словників
merged_dict = {**a, **b}
print("Об'єднаний словник:")
print(merged_dict)
