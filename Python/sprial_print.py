# this is sprial matrix printed in the order like peeling the onion 
def sprial_print(matrix):
    if matrix is None:
        return []
    # this stores the values one by one 
    result = []
    # these four pointer define the front and end of  rows and column 
    top = 0 # front of row 
    bottom = len(matrix) - 1 # end of row
    left  = 0 # front of column
    right = len(matrix[0]) - 1 # end of column
    # these condition defines the peeling the matrix values like onion 
    while top <= bottom and left <= right:
        for col in range(left,right+1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top,bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right,left - 1,-1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom,top - 1,-1):
                result.append(matrix[row][left])
            left += 1

    return result 
# i have added a custom input value for matrix 
rows  = int(input("Enter the number of rows :"))
column = int(input("Enter the number of column :"))
# custom values are stored in the order of individual rows and made the matrix according to column so even matrix only allowd rows == column
matrix = []
print("Enter the space separated row values :")
for i in range(rows):
    rows = list(map(int,input().split()))
    # this is optional only to handle error if its not a square matrix 
    if len(rows) != column:
        raise ValueError("Row must be exactcly {} element".format(column))
    matrix.append(rows)
# final output is printed after the matrix is constructed and peeled output 
print(sprial_print(matrix))
    

