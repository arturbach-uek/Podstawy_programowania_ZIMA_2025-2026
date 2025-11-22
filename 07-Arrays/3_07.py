names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

print("Names:", " ".join(names))

longest_name = names[0]
i = 1
while i < len(names):
    if len(names[i]) > len(longest_name):
        longest_name = names[i]
    i += 1

# print(names[[len(name) for name in names].index(max(len(name) for name in names))])
print("Longest name:", longest_name)
