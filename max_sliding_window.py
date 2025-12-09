from collections import deque
# arr for list of numbers and k for windows size
arr = list(map(int,input().split()))
k = int(input().strip())
def maxSlidingWindow(arr,k):
    # should mention deque to a variable so it becomes deque and can be used for LIFO
    # this stores the indices of the max value
    dq = deque()
    # to store the max value 
    res = []

    for i in range(len(arr)):
        # if the first element left the window its get removed from window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
    # if the current element is greater than previously stored element then remove the previously stored element
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
    # after the first element is removed from the window new element is added
        dq.append(i)
    # if the window is full add the first element which is max 
        if i >= k - 1:
            res.append(arr[dq[0]])
    return res
ans = maxSlidingWindow(arr,k)
print(*ans)

