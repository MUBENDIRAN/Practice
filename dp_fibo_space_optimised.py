# this function performs fibonacci series with space optimized using dynamic programming
def dp_fibo(n):
    # edge case handling
    if n <= 1:
        return n
    # constant values to store after each computation 
    prev1 = 0 # initial value 
    prev2 = 1 # follow up value 
    # swaping of computed values happens upto n 
    for _ in range(2,n+1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr

    return prev2 # to get final output use prev2 if sequence needed use curr
# custom input 
n = int(input("Enter the fibonacci series value :"))
dp = dp_fibo(n)
print(dp)