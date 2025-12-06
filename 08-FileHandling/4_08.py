import re
with open('files.txt') as f:
    files = f.read().splitlines()
for file in files:
    if re.search(r'\.\w{4}$', file):
        print(file)
