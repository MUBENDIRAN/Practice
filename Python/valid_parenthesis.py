s = input()
# to store the pairs and check 
stack = []
pairs = { ')' : '(', ']' : '[', '}' : '{'}
for ch in s:
    # if iterated element is first parenthesis its stored to stack list
    if ch in "([{":
        stack.append(ch)
#if not close paranthesis its get checked whether its not in stack or not equal to last element in pairs key
# if something stay like this its not complete paranthesis else its complete we pop and remove that from stack 
    elif ch in ")]}":
        if not  stack or stack[-1] != pairs[ch]:
            print("False")
            break
        else:
            stack.pop()
    # else the given char is not valid so stack list is empty or zero 
    else:
        print(len(stack) == 0)