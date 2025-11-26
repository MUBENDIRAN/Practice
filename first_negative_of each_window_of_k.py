arr = list(map(int,input().split()))
# k for duration of window
k= int(input())
# to store the negative values 
negatives = []
# we used two pointer with sliding window pointer start with zero according to first index
start = 0
for end in range(0,len(arr)):
    # if negatives found append it to negatives list since its list we can only append 
    if arr[end] < 0:
        negatives.append(end)
        # As loop goes and the iteration value gets equals to window value and its has a negative , the first negative is printed else 0
    if end - start + 1 == k:
        if negatives:
            print(arr[negatives[0]])
        else:
            print(0)
        """ if negatives list and the first negatives is finished in the first window its get removed by pop func. 
        and the start value is incremented by one for next iteration of window """
        if negatives and negatives[0] == start:
            negatives.pop(0)
        start += 1
