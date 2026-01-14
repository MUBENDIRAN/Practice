def subarray_sum_k(nums,k):
    count = 0
    curr = 0
    freq = {0:1}

    for x in nums:
        curr += x
        if curr - k in freq:
            count += freq[curr - k]
            freq[curr] = freq.get(curr,0) + 1

    return count

nums = list(map(int,input("Enter the sequence : ").split()))
k = int(input("Enter the value : "))

print("Number of pairs : ",subarray_sum_k(nums,k))