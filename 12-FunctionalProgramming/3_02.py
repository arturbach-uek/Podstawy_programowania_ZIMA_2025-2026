sentence = "I completely agree with you"
words = sentence.split()
letters_count = list(map(lambda w: len(w), words))
print(letters_count)