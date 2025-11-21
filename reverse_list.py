arr = list(map(int,input().split()))
rev = []
for i in range(len(arr)-1,-1,-1):
    rev.append(arr[i])
print(rev)