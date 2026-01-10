import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    brackets_stack = queue.LifoQueue()
    char_map = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    for char in expression:
        if char in ["{", "[", "("]:
            brackets_stack.put(char)
        elif char in ["}", "]", ")"]:
            if brackets_stack.empty():
                return False
            last_open = brackets_stack.get()
            if last_open != char_map[char]:
                    return False
    return brackets_stack.empty()

if brackets_ok(expression1):
   print(f"{expression1}: brackets ok")
else:
   print(f"{expression1}: brackets not correct")

if brackets_ok(expression2):
   print(f"{expression2}: brackets ok")
else:
   print(f"{expression2}: brackets not correct")


if brackets_ok(expression3):
   print(f"{expression3}: brackets ok")
else:
   print(f"{expression3}: brackets not correct")