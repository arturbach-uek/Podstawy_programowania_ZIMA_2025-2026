with open('./countries.txt', 'r') as file:
    for index, line in enumerate(file):
        print(f"{index+1}.{line}", end="")