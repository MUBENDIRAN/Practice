arr = list(map(int,input().split()))
 #for storing the reversed list
rev = []
# start from last goes towards last to first for reversal of list          
for i in range(len(arr)-1,-1,-1):
    # store the reversed list using append since we can add things in list using append  
    rev.append(arr[i])  
print(rev) 