import letter_counter

text = "You never get a second chance to make a first impression"
letter = 'e'

print(text)
result = letter_counter.count_letter(text, letter)
print(f"The number of letter '{letter}': {result}")
