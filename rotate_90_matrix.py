def matrix90(matrix):
    n = len(matrix)

    for  i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    for i in range(n):
        left , right = 0,len(matrix[i]) - 1
        while left < right:
            matrix[i][left],matrix[i][right] = matrix[i][right],matrix[i][left]
            left += 1
            right -= 1

rows = int(input("Enter the number of rows :"))
column = int(input("Enter the number of column :"))

matrix = []
print("Enter the space separated row values")
for i in range(rows):
    row = list(map(int,input().split()))
    if len(row) != column:
        raise ValueError("row must be exactly {} element".format(column))
    matrix.append(row)
matrix90(matrix)
print("90 degree Rotated matrix")
for row in matrix:
    print(*row)


