with open('it_company.csv') as file:
    lines = file.readlines()
for i in range(0, len(lines), 5):
    print(''.join(lines[i:i+5]), end='')
    input('Press Enter key...')
