from collections import deque
arr = list(map(int,input().split()))
k = int(input().strip())
def firstNegative(arr,k):
    dq = deque()
    res = []

    for i in range(len(arr)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        if arr[i] < 0:
            dq.append(i)
        if i >= k - 1:
            if dq:
                res.append(arr[dq[0]])
            else:
                res.append(0)
        return res
ans = firstNegative(arr,k)
print(*ans)