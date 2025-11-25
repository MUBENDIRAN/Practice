arr = list(map(int,input().split()))
k = int(input())
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k,len(arr)):
    window_sum -= arr[i - k]
    window_sum += arr[i]
    max_sum = max(max_sum , window_sum)
print(max)