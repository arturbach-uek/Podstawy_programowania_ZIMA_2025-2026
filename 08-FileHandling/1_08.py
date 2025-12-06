with open("pets.txt", "r") as file:
    total_words = sum(len(line.split()) for line in file)
    print(total_words)