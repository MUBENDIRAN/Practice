arr = list(map(int,input().split()))
# empty dict to store key and value for our duplicate 
freq = {}
for x in arr:
    if x in freq:
        # this loop runs when more than one element present
        freq[x]+=1
    else:
        # this is for new element
        freq[x] = 1
for key in freq:
    # if the element is more then once then it is duplicate
    if freq[key] > 1:
        print(key)