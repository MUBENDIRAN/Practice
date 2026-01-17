# this function searches the target value given in an sorted matrix 
def search(matrix,target):
    if not matrix:
        return False
    # this has the value of number of rows and columns
    rows = len(matrix)
    column = len(matrix[0])
    # these pointer used to start the comparison from top right corner which is ideal 
    r = 0
    c = column - 1
    # the condition checks the values is lower go left, higher go right 
    while r < rows and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1
        else:
            r += 1
    
    return False
# we get values of rows and columns to build the matrix in custom input
rows = int(input("Enter the number of rows :"))
column  = int(input("Enter the number of column :"))
# matrix values are stored in individual row values 
matrix = []
print("Enter the space separated row values")
for _ in range(rows):
    row = list(map(int,input().split()))
    # this is optional just to handle the error if not a square matrix
    if len(row) != column:
        raise ValueError("Values must be equal {} ".format(column))
    matrix.append(row)
# custom input for target as well and function is called to get the output 
target = int(input("Enter the target value to be searched :"))
print("the given target value is found :",search(matrix,target))