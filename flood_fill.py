def flood_fill(image,sr,sc,new):
    original = image[sr][sc]
    if original == new:
        return image

    row = len(image)
    col = len(image[0])

    def dfs(r,c):
        if r < 0 or r >= row or c < 0 or c >= col:
            return 
        if image[r][c] != original:
            return

        image[r][c] = new

        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    dfs(sr,sc)
    return image

rows = int(input("Enter the number of rows :"))
column = int(input("Enter the number of column :"))

image = []
print("Enter the desired image values :")
for _ in range(rows):
    row = list(map(int,input().split()))
    if len(row) != column:
        raise ValueError("The value you have entered is not square matrix".format(column))
    image.append(row)

sr = int(input("Enter the desired row index :"))
sc = int(input("Enter the desired column index :"))

new = int(input("Enter the new value should be filled :"))

print("Flood Filled image")
f = flood_fill(image,sr,sc,new)
for row in f:
    print(*row)