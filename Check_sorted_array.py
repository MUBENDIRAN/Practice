arr=list(map(int,input().split()))
is_sorted=True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted=False  
        break
if is_sorted:
    print('Sorted')
else:
    print('Not Sorted')