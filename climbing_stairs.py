def climb_stairs(n):
    if n <= 1:
        return n

    prev1 = 1
    prev2 = 1

    for _ in range(2,n+1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr

    return prev2

n = int(input("Enter the number of ways :"))

print(climb_stairs(n))