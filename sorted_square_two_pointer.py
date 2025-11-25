arr = list(map(int,input().split()))
left = 0
right = len(arr) - 1
# since we to store the sorted square values we need exact empty of original list
result = [0] * len(arr)
# As we gonna store values from highest to lowest we start from  last index 
pos = len(arr) - 1
while left <= right:
    # if the negative element absolute is higher than right then square will be higher the same so we add the higher first 
    if abs(arr[left]) > abs(arr[right]):
        result[pos] = arr[left] * arr[left]
        # after addition the element removed the left point moves futher
        left += 1
    else:
        result[pos] = arr[right] * arr[right]
        # if right element added it decreased to left for next element
        right -= 1
    # since element must fill one by one in sorted order in the copy of list which is empty 
    pos -= 1
print(result)