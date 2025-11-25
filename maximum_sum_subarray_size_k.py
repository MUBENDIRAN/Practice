arr = list(map(int,input().split()))
# number of consecutive for the maximum subarray
k = int(input())
# since array ends at k and starts at the respective loop iteration
window_sum = sum(arr[:k])
# to store the window_sum iterated values and used for future refernce
max_sum = window_sum
# since we used k for consecutive suming the index starts from k as first iteration has the element upto k as per window_sum
for i in range(k,len(arr)):
    # this removes the previous iterated element by subtracting with the current iteration element
    window_sum -= arr[i - k]
    # this add the new iterated element
    window_sum += arr[i]
    # window_sum last iterated value and already stored max_sum of consecutive sum values are found using max function to get the maximum 
    max_sum = max(max_sum , window_sum)
print(max_sum)