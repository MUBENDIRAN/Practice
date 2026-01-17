arr=list(map(int,input().split()))
for i in range(len(arr)):
    # iteration starts from 0 to last before of before iterated since the last contains already iterated so no need of loop
    for j in range(0,len(arr) - i - 1):
        # if previous is bigger than next then swaping occurs
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1], arr[j]
print(arr)