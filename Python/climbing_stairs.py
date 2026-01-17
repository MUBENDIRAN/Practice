# this function performs fibonacci similar opertion in space optimised with initial constant value change 
def climb_stairs(n):
    # edge case handling
    if n <= 1:
        return n
    # we use two variable to store constants
    prev1 = 1 # initial value since if there are 0 ways then only one way exist 
    prev2 = 1 # follow up value if there is 1 way then forcefully we should go that way so one 
    # this compute the ways similar to fibonacci 
    for _ in range(2,n+1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr

    return prev2 # this provide the final output 
# custom input 
n = int(input("Enter the number of ways :"))
print(climb_stairs(n))