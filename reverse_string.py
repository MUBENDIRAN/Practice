s=input()
# unlike digits we used empty string to store string 
rev=""
#iteration starts from last index
i=len(s)-1
while i >= 0:
    # to store the last iterated element
    ch=s[i]
    # to store the iterated element with the previous
    rev=rev+ch
    # this iterate by leaving the looped element
    i-=1
print(rev)
