with open("countries.txt", "r") as file:
    print(sorted([line.split(",")[0] for line in file]))