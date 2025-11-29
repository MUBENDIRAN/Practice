arr = list(map(int,input().split()))
target = int(input())
left = 0
right = len(arr) - 1
# temp. value before storing the actual floor value 
floor_val = -1
while left <= right:
    mid = (left + right) // 2
    # if target value is greater than mid then floor value we got 
    if arr[mid] <= target:
        floor_val = arr[mid]
        # but still we need the best and suitable floor value for the target so we go towards right to find the perfect
        left = mid + 1
    else:
    # if value is higher than target then we move towards left to find the approprirates
        right = mid - 1
print(floor_val)