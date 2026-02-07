# this function holds the operation of finding the floor and ceil 
def floor_ceil(arr,x):
    floor = None
    ceil = None
    # loops through
    for i in arr:
        # floor is the smallest 
        if  i <= x:
            floor = i
        # finding the highest of highest in the given 
        if i >= x and ceil is None:
            ceil = i

    return floor, ceil
# custom input
arr=list(map(int,input("Enter the sequence :").split()))
x = int(input("Enter the number :"))
print(floor_ceil(arr,x))