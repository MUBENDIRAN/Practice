arr = list(map(int,input().split()))
left = 0
right = len(arr) - 1
while left < right:
    mid = (left + right) // 2
    # As the mountain peak will be lesser in left and higher in right we use such condition 
    if arr[mid] < arr[mid + 1]:
        # if condition satisfies we move towards right to find the highest peak
        left = mid + 1
    else:
        # if not the current mid element is what actually the peak since its a unimodal sorted mountain array
        right = mid 
print(left)