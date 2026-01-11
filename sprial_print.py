def sprial_print(matrix):
    if matrix is None:
        return []

    result = []

    top = 0
    bottom = len(matrix) - 1
    left  = 0
    right = len(matrix[0]) - 1

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

rows  = int(input("Enter the number of rows :"))
column = int(input("Enter the number of column :"))

matrix = []
print("Enter the space separated row values :")
for i in range(rows):
    rows = list(map(int,input().split()))
    if len(rows) != column:
        raise ValueError("Row must be exactcly {} element".format(column))
    matrix.append(rows)

print(sprial_print(matrix))
    

