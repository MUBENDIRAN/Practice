arr = list(map(int,input().split()))
left = 0
right = len(arr) - 1
# A temp. value since we gonna replace with the found value
first_bad = -1
while left <= right:
    mid = ( left + right) // 2
    # since we need to find the bad which is denoted as 1 we made condition to 1
    if arr[mid] == 1:
        first_bad = mid
        # As we need to find the first bad we move towards left as the bad found earlier
        right = mid - 1
    else:
        # if bad not found we move towards right to find the bad of first
        left = mid + 1
# this prints the index of first bad 
print(first_bad)