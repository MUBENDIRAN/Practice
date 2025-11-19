s=input()
counter=0
vowels='aeiouAEIOU'
for ch in s:
    if ch in vowels:
        counter+=1
print(counter)