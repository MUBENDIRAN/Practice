# this function performs fibonacci series with Big O of N space complexity with dynamic programming 
def dp_fibo(n):
    # edge case handling
    if n <= 1:
        return n
    # we create empty list to store the series of computed values 
    dp = [0]*(n+1)
    dp[0] = 0 # initial value 
    dp[1] = 1 # follow up value 
    # loop to compute fibonacci values and stored in dp so no recomputing of subproblems 
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n] # to get final output of final value use n else just dp 
# custom input 
n = int(input("Enter the fibonacci series value : "))
dp  = dp_fibo(n)
print(dp)