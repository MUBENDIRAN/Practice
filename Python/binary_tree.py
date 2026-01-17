arr = list(map(int,input().split()))
# number to be searched 
num = int(input())
left = 0
right = len(arr) - 1
while left < right:
    # since binary start from middle 
    mid = (left + right) // 2
    # if middle element is lesser then move the right pointer 
    if arr[mid] < num:
        right = mid + 1
    # if middle element is higher then move the left pointer
    elif arr[mid] > num:
        left = mid - 1
    else:
        print(mid)
        break
# this is for safe fail 
else:
    print(-1)