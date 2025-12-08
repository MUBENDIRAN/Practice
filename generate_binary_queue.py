# we use deque from library so we can use queue in O(1)
from collections import deque
n = int(input())
def generateBinary(n):
    # Asign q to deque so we can use q for deque operations
    q = deque()
    # since we generate binary from 1 to N the append the initial value 1
    q.append("1")
    # since index value is not important we use _ (underscore)
    for _ in range(n):
        # we store the first binary element to add with its child element to make a series of continuous binary of N like DFS 
        curr = q.popleft()
        print(curr)
        q.append(curr + "0")
        q.append(curr + "1")
generateBinary(n)