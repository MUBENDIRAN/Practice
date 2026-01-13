# this function performs the longest increasing subsequence 
def length_lis(nums):
    # to handle edge cases 
    n = len(nums)
    if n  == 0:
        return 0
    # this create a n length of 1 so every element alone is LIS of length one 
    dp = [1]*n
    # the outer loop handles the follow up values and inner loop helps in finding the subsequence with value of i so within range 
    for i in range(n):
        for j in range(i):
            # this checks whether left is lower and right is higher if then i is the starting point from there sequence starts 
            if nums[j] < nums[i]:
                dp[i] = max(dp[i] , dp[j] + 1)

    return max(dp) # from the list the max is the answer 
# custom sequence of input 
nums = list(map(int,input("Enter the sequence :").split()))
print(length_lis(nums))