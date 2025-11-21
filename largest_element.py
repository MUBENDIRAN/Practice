ar=list(map(int,input().split()))
# asign first value so we can compare the largest or smallest in an array
max_value=ar[0]
for i in range(1,len(ar)):
    if ar[i] > max_value:
        max_value=ar[i]
print(max_value)