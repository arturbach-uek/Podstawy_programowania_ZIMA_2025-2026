def get_acronym(name):
    return "".join(word[0] for word in name.split())

print(get_acronym("Internet of Things"))