num=int(input())
n=str(num)
for a in n:
    # used slicing for convenience 
    st=n[::-1]
if n == st:
    print("Palindrome")
else:
    print("Not Palindrome")