###
# A program that prints a numerical representation of each letter of your name.
#
name = 'Artur' # replace John with your name
# print(f'The letter {name[0]} has a code {ord(name[0])}')
# print(f'The letter {name[1]} has a code {ord(name[1])}')
for letter in name:
    print(f'The letter {letter} has a code {ord(letter)}')