s = input()
stack = []
for ch in s:
    stack.append(ch)
rev = ""
while stack:
    stack.pop()
print(rev)