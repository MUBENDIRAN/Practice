arr=list(map(int,input().split()))
largest=arr[0]
for i in range(1,len(arr)):
    if arr[i] > largest:
        largest=arr[i]
# since the second largest must be lesser than largest and greater than others we used the max lowest element to compare so -infinity temp place holder
second=float('-inf')
for x in arr:
    if x != largest and x > second:
        second = x
print(second)