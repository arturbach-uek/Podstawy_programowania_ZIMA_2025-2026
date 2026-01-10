def reverse_string(string):
    stack = list(string)
    reversed_s = ''
    while stack:
        reversed_s += stack.pop()
    return reversed_s

text = input("Enter text to reverse: ")
print(reverse_string(text))
