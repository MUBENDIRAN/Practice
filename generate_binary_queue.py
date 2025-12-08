from collections import deque
n = int(input())
def generateBinary(n):
    q = deque()
    q.append("1")

    for _ in range(n):
        curr = q.popleft()
        print(curr)
        q.append(curr + "0")
        q.append(curr + "1")
generateBinary(n)