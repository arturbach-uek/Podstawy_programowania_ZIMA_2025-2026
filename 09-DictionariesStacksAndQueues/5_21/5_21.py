import json

favourite = {
    "title": "Harry Potter and the Philosopher's Stone",
    "author": "J.K. Rowling",
    "year": 1997,
    "genre": "Fantasy",
    "rating": 9.0
}

with open('favourite.json', 'w', encoding='utf-8') as file:
    json.dump(favourite, file, indent=4)

print("Favourite book/movie saved")
