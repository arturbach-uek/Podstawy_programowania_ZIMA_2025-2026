phone_book = {
    'John': '555-1234',
    'David': '555-5678',
    'Bob': '555-8765',
    'Charlie': '555-4321',
    'Diana': '555-9876',
    'Daniel': '555-4444',
    'Dominic': '555-1010'
}

for name, number in phone_book.items():
    if name.startswith("D"):
        print(name, number)
