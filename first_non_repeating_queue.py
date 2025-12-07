# we used a built in functions for queue for easy implementation
from collections import deque
stream = list(map(int,input().split()))
# this function handles both queue and hashmap
def firstNonRepeating(stream):
    # deque for first element poping and freq hashmap is for finding unique values with their frequency
    q = deque()
    freq = {}
    # this loop goes through all element and add to freq if already available add 1 else add the element with 1 
    for ch in stream:
        freq[ch] = freq.get(ch,0) + 1
    # this ensure both q and freq has all elements
        q.append(ch)
    # if q is not empty and freq of the q element is more than one then those elements are removed 
    while q and freq[q[0]] > 1:
        q.popleft()
    # after the removal still any element is left print the first element present else -1 
    if q:
        print(q[0])
    else:
        print(-1)

firstNonRepeating(stream)