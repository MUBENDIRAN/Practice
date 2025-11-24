arr = list(map(int,input().split()))
pos=1
for i in range(1,len(arr)):
    if arr[i] != arr[i-1]:
        arr[pos] = arr[i]
        pos += 1
print(pos)
print(arr)