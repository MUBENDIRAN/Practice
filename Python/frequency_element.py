arr=list(map(int,input().split()))
# we have used dictionary since we need key pair representation as the value is constant and frequency alone changes 
freq={}
for x in arr:
    if x in freq:
        # this happens when already the value is stored with its frequency
        freq[x]+=1
    else:
        # this happens when new value is stored in the dictionary
        freq[x] = 1
# we used another loop since we can change the format of the output as we want best practice 
for key in freq:
    print(key,freq[key])