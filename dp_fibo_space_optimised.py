def dp_fibo(n):
    if n <= 1:
        return n

    prev1 = 0
    prev2 = 1

    for _ in range(2,n+1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr

    return prev2

n = int(input("Enter the fibonacci series value :"))
dp = dp_fibo(n)
print(dp)