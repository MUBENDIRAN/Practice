arr=list(map(int,input().split()))
freq={}
for x in arr:
    if x in freq:
        freq[x]+=1
    else:
        freq[x] = 1
for key in freq:
    print(key,freq[key])
print(freq)