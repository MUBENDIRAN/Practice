def length_lis(nums):
    n = len(nums)
    if n  == 0:
        return 0

    dp = [1]*n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i] , dp[j] + 1)

    return max(dp)

nums = list(map(int,input("Enter the sequence :").split()))
print(length_lis(nums))