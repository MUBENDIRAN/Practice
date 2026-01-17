# this function holds the operation of finding the length of longest linear values that makes sum to zero
def longest_sum_zero(nums):
    curr = 0 # holds the prefix sum value
    first = {0:-1} # this makes the problem optimized
    best = 0 # holds the length of longest length 

    for i in range(len(nums)):
        x = nums[i]
        curr += x
        if curr in first: 
            best = max(best,i - first[curr]) # if curr found add the initial -1 to i so we get new length 
        else:
            first[curr] = i # not found add the value to hashmap
        
    return best
# custom input 
nums = list(map(int,input("Enter the sequence : ").split()))
print("Longest sequence of sum  of 0 :",longest_sum_zero(nums))