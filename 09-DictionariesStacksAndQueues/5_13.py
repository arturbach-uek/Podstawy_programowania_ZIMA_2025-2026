def evaluate_rpn():
    stack = []
    while True:
        token = input("Enter number/operator/= : ")
        if token == "=":
            print("Result:", stack.pop())
            break
        elif token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == "+": stack.append(a+b)
            elif token == "-": stack.append(a-b)
            elif token == "*": stack.append(a*b)
            elif token == "/": stack.append(a/b)
        else:
            stack.append(float(token))

evaluate_rpn()
