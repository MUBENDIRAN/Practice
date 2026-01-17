s=input()
counter=0
#we use a continous single string of vowels so it read like english so time complexity we can use single char representation too
vowels='aeiouAEIOU'
for ch in s:
    if ch in vowels:
        counter+=1
print(counter)