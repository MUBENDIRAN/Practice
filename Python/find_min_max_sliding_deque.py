from collections import deque
arr = list(map(int,input().split()))
k = int(input().strip())
def sumMinMax(arr,k):
    # we have use deque to declare to a variable so it can be used as deque 
    maxDq = deque()
    minDq = deque()
    res = []

    for i in range(len(arr)):
        # if ensure that the first element went from the window is removed to new element can be added
        if maxDq and maxDq[0] < i - k + 1:
            maxDq.popleft()
        # if ensure that the first element went from the window is removed to new element can be added
        if minDq and minDq[0] < i - k + 1:
            minDq.popleft()
        # if the current element is greater than the stored previous then the previous one is poped and replaced 
        while maxDq and arr[i] >= arr[maxDq[-1]]:
            maxDq.pop()
         # if the current element is smaller than the stored previous then the previous one is poped and replaced 
        while minDq and arr[i] <= arr[minDq[-1]]:
            minDq.pop()
        # new element is added in both end for max and min 
        maxDq.append(i)
        minDq.append(i)
        # if the window size is reached both the current max and min element is added and appended to res
        if i >= k - 1:
            res.append(arr[maxDq[0]] + arr[minDq[0]])
    return res
ans = sumMinMax(arr,k)
print(*ans)