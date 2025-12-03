arr = list(map(int,input().split()))
for i in range(len(arr)):
    min_val = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min_val]:
            min_val = j
    arr[i],arr[min_val] = arr[min_val],arr[i]
print(arr)