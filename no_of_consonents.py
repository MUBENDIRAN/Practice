s=input()
count=0
vowels='aeiouAEIOU'
for ch in s:
    if ch.isalpha() and ch not in vowels:
        count+=1
print(count)