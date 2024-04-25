data = [
    1952, 1000000,
    10.45, 5.5,
    (2+3j),
    False,
    "pythonguide.pp.ua",
    (1, -6),
    [3, 15],
    {'Class C': ['Volkswagen Golf', 'Ford Focus'], 'Class F': ['Audi A8', 'Bentley', 'Maybach'], 'E': ['Toyota Camry']}, 
    {},
    None
]

data_types = {}

for value in data:
    data_type = type(value)
    if data_type not in data_types:
        data_types[data_type] = [value]
    else:
        data_types[data_type].append(value)

print("Вихідні дані:")
for data_type, values in data_types.items():
    print(data_type, end=' ')
    for value in values:
        print(value, end=' ')
    print()
