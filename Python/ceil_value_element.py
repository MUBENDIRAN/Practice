arr = list(map(int,input().split()))
target = int(input())
left = 0
right = len(arr) - 1
# similar to floor temp. value before storing the ceil  actual value
ceil_val = -1
while left <= right:
    mid = (left + right) // 2
    # if value is greater than target we can find the ceil of the element by moving towards left to match accurate ceil value
    if arr[mid] >= target:
        ceil_val = arr[mid]
        right = mid - 1
    else:
    # if the value is smaller than target then move towards the left to find the accurate value 
        left = mid + 1
print(ceil_val)