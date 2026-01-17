arr = list(map(int,input().split()))
# target number to be found first and last 
target = int(input())
# two pointer and variable first with some value for temp.
left = 0 ; right = len(arr) - 1 ; first = -1
while left <= right:
    mid = (left + right ) // 2
    if arr[mid] == target:
        # if value found temp. variable is replaced by its index
        first = mid
        # And previous value is searched by reducing right and moving towards left  
        right = mid - 1
    elif arr[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
# Similarly to last too tmep. variable
left = 0 ; right = len(arr) - 1 ; last = -1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        # similarly to last the temp. variable is replaced by index found 
        last = mid
    # left value is increased so search towards right to find the last value 
        left = mid + 1
    elif arr[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
print(first,last)