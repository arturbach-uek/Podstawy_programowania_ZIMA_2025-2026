import my_text

text = "An apple a day keeps the doctor away"

print("Text:", text)
print("Number of words:", my_text.word_count(text))
print("Words from the longest:", ", ".join(my_text.words_by_length(text)))
print("Words ordered alphabetically:", ", ".join(my_text.words_alphabetically(text)))
