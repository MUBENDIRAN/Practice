# this function handles the operation of finding the number of pairs have sum of k 
def subarray_sum_k(nums,k):
    count = 0 # has the count of pairs
    curr = 0 # holds the prefix sum value
    freq = {0:1} # this make the problem optimised 

    for x in nums:
        curr += x
        if curr - k in freq: # this is a math formula previous - current = k so previous - k = current 
            count += freq[curr - k]  # counts the numbber of pairs
            freq[curr] = freq.get(curr,0) + 1 # adds the curr - k value and curr value 

    return count
# custom input 
nums = list(map(int,input("Enter the sequence : ").split()))
k = int(input("Enter the value : "))

print("Number of pairs : ",subarray_sum_k(nums,k))