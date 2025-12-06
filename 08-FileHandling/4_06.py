filename = input("Enter file name: ")
try:
    with open(filename) as file:
        text = file.read()
    lines = text.splitlines()
    words = text.split()
    print(f"File name: {filename}")
    print(f"Number of lines: {len(lines)}")
    print(f"Number of characters: {len(text)}")
    print(f"Number of words: {len(words)}")
except FileNotFoundError:
    print("File not found")
