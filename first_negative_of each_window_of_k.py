arr = list(map(int,input().split()))
k= int(input())
negatives = []
start = 0
for end in range(0,len(arr)):
    if arr[end] < 0:
        negatives.append(end)
    if end - start + 1 == k:
        if negatives:
            print(arr[negatives[0]])
        else:
            print(0)
        if negatives and negatives[0] == start:
            negatives.pop(0)
        start += 1
