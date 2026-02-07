def floor_ceil(arr,x):
    floor = None
    ceil = None

    for i in arr:
        if  i <= x:
            floor = i
        if i >= x and ceil is None:
            ceil = i

    return floor, ceil

arr=list(map(int,input("Enter the sequence :").split()))
x = int(input("Enter the number :"))
print(floor_ceil(arr,x))