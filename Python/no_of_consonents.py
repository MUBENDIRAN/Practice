s=input()
count=0
# we use a continous single string of vowels so it read like english so time complexity we can use single char representation too
vowels='aeiouAEIOU'
for ch in s:
    # since consonants are non vowels character and to avoid non character elements we used isalpha function
    if ch.isalpha() and ch not in vowels:
        count+=1
print(count)