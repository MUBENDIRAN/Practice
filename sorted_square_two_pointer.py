arr = list(map(int,input().split()))
left = 0
right = len(arr) - 1
result = [0] * len(arr)
pos = len(arr) - 1
while left <= right:
    if abs(arr[left]) > abs(arr[right]):
        result[pos] = arr[left] * arr[left]
        left += 1
    else:
        result[pos] = arr[right] * arr[right]
        right -= 1
pos -= 1
print(result)