arr = list(map(int,input().split()))
for i in range(len(arr)):
    # during the first iteration the first iterated value is stored 
    min_val = i
    # As first value is stored iteration starts from second
    for j in range(i+1,len(arr)):
        # if previous stored value is higher than next then the previously stored value is replaced with the lower
        if arr[j] < arr[min_val]:
            min_val = j
        # if there change or no change accordingly the swaping takes place
    arr[i],arr[min_val] = arr[min_val],arr[i]
print(arr)