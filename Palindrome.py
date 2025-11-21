num=int(input())
# stored in separate variable since num is modified when loop runs
original=num
rev=0
#loop runs when there is non zero 
while num > 0:
    # this separate the last digit one by one maths trick numbers represented in 10's
    digit = num % 10
    # As we add up one by one in order the mutiplication of 10's must happen to get the proper reversal of digits
    rev = rev*10 + digit 
    # this is used so the original is modified and the last looped element is droped so loop wont go infinite
    num = num // 10
if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
