arr = list(map(int,input().split()))
target=int(input())
left=0
right=len(arr) -1
while left < right:
    curr_total = arr[left]+arr[right]
    if curr_total == target:
        print(arr[left],arr[right])
        break
    elif curr_total < target:
        left+=1
    else:
        right-=1