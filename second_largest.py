arr=list(map(int,input().split()))
largest=arr[0]
for i in range(1,len(arr)):
    if arr[i] > largest:
        largest = arr[i]
second=float('-inf')
for x in arr:
    if x != largest and x > second:
        second = x
print(second)