def search(matrix,target):
    if not matrix:
        return False

    rows = len(matrix)
    column = len(matrix[0])

    r = 0
    c = column - 1

    while r < rows and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1
        else:
            r += 1
    
    return False

rows = int(input("Enter the number of rows :"))
column  = int(input("Enter the number of column :"))

matrix = []
print("Enter the space separated row values")
for _ in range(rows):
    row = list(map(int,input().split()))
    if len(row) != column:
        raise ValueError("Values must be equal {} ".format(column))
    matrix.append(row)

target = int(input("Enter the target value to be searched :"))
print("the given target value is found :",search(matrix,target))