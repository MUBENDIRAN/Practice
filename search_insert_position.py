arr = list(map(int,input().split()))
# Target number to be inserted
target = int(input())
left = 0
right = len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    # if number already found no need to find the index to insert just replace with the old index
    if arr[mid] == target:
        print(mid)
        break
    # if not and lower than mid go through left
    elif target < arr[mid]:
        right = mid - 1
    else:
        # if higher and not found go through right 
        left = mid + 1
# this give the index where the element must be stored to be sorted
print(left)