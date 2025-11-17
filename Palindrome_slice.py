num=int(input())
n=str(num)
for a in n:
    st=n[::-1]
if n == st:
    print("Palindrome")
else:
    print("Not Palindrome")