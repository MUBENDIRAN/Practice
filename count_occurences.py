arr = list(map(int,input().split()))
target = int(input())
left = 0 
right = len(arr) - 1
# like first occurence we used a temp. value before actual
first = -1
while left <= right:
    mid = (left + right) // 2
    # if target found in mid itself just change first and go through left to find the actual first
    if arr[mid] == target:
        first = mid
        right = mid - 1
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
left = 0
right = len(arr) - 1  
# like last occurence we used a temp. value before actual
last = -1
while left <= right:
    mid = (left + right) // 2
    # if target found in the mid itself just change the last and go through the right to find the actual last
    if arr[mid] == target:
        last = mid
        left = mid + 1
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
# this formula helps to find the occurence like we use in sliding window "end - start + 1"
num = last - first + 1
print(num) 