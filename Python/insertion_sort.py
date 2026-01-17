arr = list(map(int,input().split()))
# Since the first element is sorted anyway since no element to compare 
for i in range(1,len(arr)):
    # first iteration is stored to compare
    key = arr[i]
    # second is stored to compare
    j = i - 1
    # while j is equal and more then zero, when a element present and current is compared with the previous and higher next element made to present
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        # then the j is reduced to compare with previous of next iterated value
        j-=1
    # key value is changed with changed value which is compared with the previous
    arr[j+1] = key
print(arr)