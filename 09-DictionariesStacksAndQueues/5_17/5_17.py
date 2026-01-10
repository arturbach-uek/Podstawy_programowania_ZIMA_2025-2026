import json

with open('cities.json', 'r', encoding='utf-8') as file:
    cities = json.load(file)

for city in cities:
    for key, value in city.items():
        print(f"{key}: {value}")
    print()