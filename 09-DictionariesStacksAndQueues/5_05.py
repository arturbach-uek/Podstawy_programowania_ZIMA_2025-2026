paragraph = "cat dog mouse cat rat cat mouse"
words = paragraph.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(count)
