from collections import deque
arr = list(map(int,input().split()))
k = int(input().strip())
def firstNegative(arr,k):
    # it stores the indices of negatives
    dq = deque()
    # it stores the negative value
    res = []

    for i in range(len(arr)):
        # if the first element is left the window its get removed from the list
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        # if the current element is negative its indices it appended to dq
        if arr[i] < 0:
            dq.append(i)
        # if the window is full the negatives value is appended to res 
        if i >= k - 1:
            if dq:
                res.append(arr[dq[0]])
            else:
                res.append(0)
    return res
ans = firstNegative(arr,k)
print(*ans)