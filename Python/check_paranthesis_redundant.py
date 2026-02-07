# this function holds the operation of finding the expression redundant paranthesis with boolean output
def is_redundant(expr):
    stack = [] # to store the values and operate stack operation
    # this loop through the expression
    for ch in expr:
        # once the stack has the expression the condition to finding the redundant applies
        if ch == ')':
            # to check extra ")" is available in stack
            if not stack:
                return "Invalid"
            has_operator = False
            top = stack.pop()
            # loop runs untill the valid pair is found
            while top != '(':
                if top in "+-*/": # to check whether operator is found or not 
                    has_operator = True
                # to check extra "(" is available in stack
                if not stack:
                    return "Invalid"
                top = stack.pop()

            if not has_operator:
                return True

        else: # first the expression is appenended and the stack operation is held
            stack.append(ch)
    # to avoid to extra parantheis
    if '(' in stack:
        return "Invalid"

    return False
# custom input
expr = input("Enter the expersion :")
print(is_redundant(expr))


