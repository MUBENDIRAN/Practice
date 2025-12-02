n = int(input()) 
# since we gonna calculate it for integer not an array pointer start with one not zero 
left = 1
# since the length can be any we used right the last pointer as n for its length
right = n
# we used a temp. value before actual 
ans = 0
while left <= right:
    mid = (left + right) // 2
    # It searches the mid index and compare with the given integer, if it matches its perfect square so loop ends
    if mid*mid == n:
        ans = mid
        break
    # if value lesser move towards right
    elif mid*mid < n:
        # its has the possible square before moving 
        ans = mid
        left = mid + 1
    else:
        # if the value is higher move towards left
        right = mid - 1
print(ans)
