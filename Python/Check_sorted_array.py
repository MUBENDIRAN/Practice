arr=list(map(int,input().split()))
# Set a variable to a boolean true so we can use different conditions to satisfy this condition
is_sorted=True
#since we are comparing two values we use last before value for the final loop 
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted=False  
        break # we use break if not sorted and leave the loop
if is_sorted:
    print('Sorted')
else:
    print('Not Sorted')