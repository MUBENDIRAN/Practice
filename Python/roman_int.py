def roman_int(num):
    values =  {
        'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
    }

    total = 0
    for i in range(len(num) - 1):
        if values[num[i]] < values[num[i+1]]:
            total -= values[num[i]]
        else:
            total += values[num[i]]

    total += values[num[-1]]
    return total

num = input("Enter the Roman value :")
print(roman_int(num))