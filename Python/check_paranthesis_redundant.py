def is_redundant(expr):
    stack = []

    for ch in expr:
        if ch == ')':
            top = stack.pop()
            has_operator = False

            while top != '(':
                if top == "+-*/":
                    has_operator = True
                top = stack.pop()

            if not has_operator:
                return True

        else:
            stack.append(ch)

    return False

expr = input("Enter the expersion :")
print(is_redundant(expr))


