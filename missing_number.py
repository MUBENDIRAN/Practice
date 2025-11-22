arr = list(map(int,input().split()))
N = len(arr) + 1
expected = N * (N + 1) // 2
actual = sum(arr)
missing = expected - actual 
print (expected)
print(actual)
print(missing)