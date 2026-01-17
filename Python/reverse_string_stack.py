s = input()
# to store the elements in LIFO
stack = []
for ch in s:
    #each element is iterated and added to stack
    stack.append(ch)
# to store the reverse charater
rev = ""
# when stack has elements its get poped from last and stored in rev so we get reverse of the element
while stack:
    rev += stack.pop()
print(rev)