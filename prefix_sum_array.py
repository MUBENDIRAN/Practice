n = int(input())
arr = list(map(int,input().split()))
prefix = []
max_sum = 0
for x in arr:
    max_sum += x
    prefix.append(max_sum)
print(max_sum)