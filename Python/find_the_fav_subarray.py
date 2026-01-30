def derive_number(subarray):
    strs = list(map(str,subarray))

    max_len = max(len(s) for s in strs)

    padded = [s.zfill(max_len) for s in strs]

    result_digit = []
    for i in range(max_len):
        max_digit = max(int(num[i]) for num in padded)
        result_digit.append(str(max_digit))

    return int("".join(result_digit))

def find_valid_subarray(arr,k,fav):
    valid = []
    invalid = []

    print("Subarray and derived numbers:")
    
    for i in range(len(arr) - k + 1):
        window = arr[i:i+k]
        derived = derive_number(window)

        print(f"{tuple(window)} -> {derived}")

        if fav in window:
            valid.append(window)
        else:
            invalid.append(window)


    print("Valid subarray")
    for v in valid:
        print(v)

    print("Invalid subarray")
    for iv in invalid:
        print(iv)

arr = list(map(int,input("Enter the array of values :").split()))
k = int(input("Enter the window size :"))
fav = int(input("Enter the fav number :"))

find_valid_subarray(arr,k,fav)