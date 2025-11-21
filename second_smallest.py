arr=list(map(int,input().split()))
smallest=arr[0]
for i in range(1,len(arr)):
    if arr[i] < smallest:
        smallest=arr[i]
# similar to second largest to compare with max largest to get the second smallest we use +infinity a temperory place holder
second=float('inf')
for x in arr:
    if x != smallest and x < second:
        second = x
print(second)