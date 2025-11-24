arr = list(map(int,input().split()))
# since we gonna sort by keeping the non zero one side and zeros other we start from index zero 
pos = 0
for i in range(len(arr)):
    # this loop arranges the non zeros towards the first by replacing the empty spaces without changing order and new list
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1
# this loop creates the empty space at last according to list created 
for i in range(pos,len(arr)):
        arr[i] = 0
print(arr)