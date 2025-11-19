s=input()
rev=""
i=len(s)-1
while i>= 0:
    ch=s[i]
    rev=rev+ch
    i-=1
print(rev)
