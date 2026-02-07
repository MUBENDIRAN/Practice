# this function holds the operation of converting the roman to integer
def roman_int(num):
    # dict to store the roman and equivalent value
    values =  {
        'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
    }

    total = 0
    # loop through
    for i in range(len(num) - 1):
        # roman condition calculate from right to left so small means minus withe previous total 
        if values[num[i]] < values[num[i+1]]:
            total -= values[num[i]]
        else: # if higher add
            total += values[num[i]]
    # calculate from the last ( right to left)
    total += values[num[-1]]
    return total
# custom input
num = input("Enter the Roman value :")
print(roman_int(num))