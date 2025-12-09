from collections import deque
arr = list(map(int,input().split()))
k = int(input().strip())
def sumMinMax(arr,k):
    maxDq = deque()
    minDq = deque()
    res = []

    for i in range(len(arr)):
        if maxDq and maxDq[0] < i - k + 1:
            maxDq.popleft()

        if minDq and minDq[0] < i - k + 1:
            minDq.popleft()

        while maxDq and arr[i] >= arr[maxDq[-1]]:
            maxDq.pop()
        
        while minDq and arr[i] <= arr[minDq[-1]]:
            minDq.pop()
        
        maxDq.append(i)
        minDq.append(i)

        if i >= k - 1:
            res.append(arr[maxDq[0]] + arr[minDq[0]])
    return res
ans = sumMinMax(arr,k)
print(*ans)