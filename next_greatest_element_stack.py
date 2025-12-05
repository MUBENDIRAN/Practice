arr = list(map(int,input().split()))
stack = []
result = len(arr) * [-1]
for i in range(len(arr)):
    while stack and arr[i] > arr[stack[-1]]:
        idx = stack.pop()
        result[idx] = arr[i]
    stack.append(i)
print(*result)
