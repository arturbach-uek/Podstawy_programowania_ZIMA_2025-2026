def word_count(text):
    return len(text.split())

def words_by_length(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)

def words_alphabetically(text):
    words = text.split()
    return sorted(words)
