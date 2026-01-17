arr = list(map(int,input().split()))
target = int(input())
left = 0
# since we dont know the length of array we used a temp. value untill we find the nearest value of target
right = 1
# This while loop helps in finding the nearest value of target without time complexity it loops in exponential to less time to find the nearest value 
while arr[right] < len(arr) and arr[right] < target:
    # since the value is not nearby we make starting and ending point together to make the searching window small 
    left = right 
    # As the target value is not near we increase the end point exponentially to find the nearest value of target 
    right = right * 2
# after finding the nearest value of target we get a new set of searching window to find the target using normal binary search
    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == target:
            print(mid)
            break
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            print(-1)