# this problem works when array is 1 to N ,no duplicates ,no extra values than N 
arr = list(map(int,input().split()))
# since one number missing which is len -1 so we used len + 1 to calculate 
N = len(arr) + 1
# basic maths formula for finding missing number
expected = N * (N + 1) // 2
actual = sum(arr)
missing = expected - actual 
print(missing)