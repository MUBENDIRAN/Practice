arr = list(map(int,input().split()))
target=int(input())
left=0
right=len(arr) -1
while left < right:
    curr_total = arr[left]+arr[right]
    # this loop runs when target found
    if curr_total == target:
        print(arr[left],arr[right])
        break
    # this loop runs when total is lower than target so moving the left points towards right is ideal
    elif curr_total < target:
        left+=1
    # this loop runs when total is higher than target so moving the right point towards left is ideal
    else:
        right-=1