# this function holds the operation of finding the subarrays dervived number
def derive_number(subarray):
    # int is converted string in list
    strs = list(map(str,subarray))
    # finding the max length of strings
    max_len = max(len(s) for s in strs)
    # making the string equal in length to find the derived value 
    padded = [s.zfill(max_len) for s in strs]
    # this stores the derived values 
    result_digit = []
    for i in range(max_len):
        # this find the largest value in a column 
        max_digit = max(int(num[i]) for num in padded)
        result_digit.append(str(max_digit)) # appended as string 

    return int("".join(result_digit)) # derived values are joined without space to make it a single string
# this function handles the operation of finding the valid subarray which consists of the fav number
def find_valid_subarray(arr,k,fav):
    valid = [] # this stores the valid subarray
    invalid = [] # this stores the invalid subarray

    print("Subarray and derived numbers:")
    # this loop separate the array as required array 
    for i in range(len(arr) - k + 1):
        window = arr[i:i+k]
        # the separated window is used as subarray to derive the number of previous function
        derived = derive_number(window)
        # this prints the window ans its respective derived value
        print(f"{tuple(window)} -> {derived}")
        # this condition finds fav found in window to be valid
        if fav in window:
            valid.append(window)
        else:
            invalid.append(window)

    # valid and invalid are printed in sequence 
    print("Valid subarray")
    for v in valid:
        print(v)

    print("Invalid subarray")
    for iv in invalid:
        print(iv)
# custom input 
arr = list(map(int,input("Enter the array of values :").split()))
k = int(input("Enter the window size :"))
fav = int(input("Enter the fav number :"))
# function returns the value of valid invalid and derived value since all the output printed in single function
find_valid_subarray(arr,k,fav)