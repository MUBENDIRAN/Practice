from collections import deque
stream = list(map(int,input().strip()))
def firstNonRepeating(stream):
    q = deque()
    freq = {}

    for ch in stream:
        freq[ch] = freq.get(ch,0) + 1
        q.append(ch)
    
    while q and freq[q[0]] > 1:
        q.popleft()

    if q:
        print(q[0])
    else:
        print(-1)