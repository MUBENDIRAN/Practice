from collections import deque
arr = list(map(int,input().split()))
class maxSlidingWindow:
    def maxSlidingWindow(arr,k):
        dq = deque()
        res = []

        for i in range(len(arr)):
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            while dq and arr[i] <= arr[dq[-1]]:
                dq.popleft()

            dq.append(i)

            if i >= k + 1:
                res.append(arr[dq[0]])
        return res

