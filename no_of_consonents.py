s=input()
count=0
vowels='aeiouAEIOU'
for ch in s:
    if ch not in vowels and ch.isalpha():
        count=+1
print(count)