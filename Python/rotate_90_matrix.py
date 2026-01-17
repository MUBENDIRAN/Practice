# this function rotate the matrix in place to 90 degrees 
def matrix90(matrix):
    n = len(matrix)
    # this nested loop transpose the matrix the first right triangle 
    for  i in range(n): # this holds the row to be transposed 
        for j in range(i,n): # this transpose the elements
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    # this loop reverse the rows of the matrix so  we get the 90 degree rotated as needed 
    for i in range(n):
        left , right = 0,len(matrix[i]) - 1 # we can use reverse function too 
        while left < right:
            matrix[i][left],matrix[i][right] = matrix[i][right],matrix[i][left]
            left += 1
            right -= 1
# we have used manual matrix input for custom input 
rows = int(input("Enter the number of rows :"))
column = int(input("Enter the number of column :"))
# we store the matrix values in each rows eqaul to column values so it beomes the square matrix 
matrix = []
print("Enter the space separated row values")
for i in range(rows):
    row = list(map(int,input().split()))
    # its optional just to handle the error occuring if not square matrix
    if len(row) != column:
        raise ValueError("row must be exactly {} element".format(column))
    matrix.append(row)
# function called and then matrix printed as rows in space separated     
matrix90(matrix)
print("90 degree Rotated matrix")
for row in matrix:
    print(*row)


