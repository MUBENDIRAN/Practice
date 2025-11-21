arr = list(map(int,input().split()))
rev = [] #for storing the reversed list
for i in range(len(arr)-1,-1,-1): # start from last goes towards last to first for reversal of list
    rev.append(arr[i])  # store the reversed list using append since we can add things in list using append 
print(rev) 