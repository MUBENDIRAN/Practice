arr = list(map(int,input().split()))
for i in range(len(arr)):
    min_val = i
    for j in range(i+1,len(arr)):
        if arr[i] < arr[min_val]:
            min_val = arr[i]
            arr[i],arr[min_val] = arr[min_val],arr[i]
print(arr)