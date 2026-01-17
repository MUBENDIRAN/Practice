arr = list(map(int,input().split()))
# since the first array [0] will always be original so comparison start from second position [1]
pos=1
for i in range(1,len(arr)):
    if arr[i] != arr[i-1]:
        # since we are not using the next list to store we use swaping of elements
        arr[pos] = arr[i]
        pos += 1
print(pos)
print(arr)