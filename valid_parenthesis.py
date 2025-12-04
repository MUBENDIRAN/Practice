s = input()
stack = []
pairs = { ')' : '(', ']' : '[', '}' : '{'}
for ch in s:
    if ch in "([{":
        stack.append(ch)
    elif ch in ")]}":
        if not  stack or stack[-1] != pairs[ch]:
            print("False")
            break
        else:
            stack.pop()
    else:
        print(len(stack) == 0)