def longest_sum_zero(nums):
    curr = 0
    first = {0:-1}
    best = 0

    for i in range(len(nums)):
        x = nums[i]
        curr += x
        if curr in first:
            best = max(best,i - first[curr])
        else:
            first[curr] = i
        
    return best

nums = list(map(int,input("Enter the sequence : ").split()))
print("Longest sequence of sum  of 0 :",longest_sum_zero(nums))