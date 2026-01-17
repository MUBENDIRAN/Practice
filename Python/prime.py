n = int(input())
if n<=1:
    print("NO")
else:
    is_prime = True
    i = 2
    while i*i <= n:
        if n%i == 0:
            is_prime = False
            break
        i+=1
    if is_prime:
        print("yes")
    else:
        print("NO")
