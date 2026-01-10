translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

word = input("Enter an English word: ").lower()
translation = translations.get(word, "Translation unavailable")
print(translation)
