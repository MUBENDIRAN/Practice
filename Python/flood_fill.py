''' this function perform the flood fill where the specific pixel or element is replaced with new so connected nodes or pixel changes the same value 
like ms paint coloring the specific connected pixels as we change the color ''' 
def flood_fill(image,sr,sc,new):
    # we store the initial original element for comparison so we dont recolor the changed one 
    original = image[sr][sc]
    # if the color or element is the one gonna change the which is already available no change 
    if original == new:
        return image
    # defining the rows and column because its matrix based 
    row = len(image)
    col = len(image[0])
    # we have used dfs since spread behaviour naturally simple no queue needed 
    def dfs(r,c):
        # edge case handling to avoid errors
        if r < 0 or r >= row or c < 0 or c >= col:
            return 
        # to avoid repaint or replacing the same element again to stop recursion
        if image[r][c] != original:
            return
        # replace the new value 
        image[r][c] = new
    # to paint the connected left, right, top, bottom
        dfs(r+1,c) # Bottom
        dfs(r-1,c) # top
        dfs(r,c+1) # right 
        dfs(r,c-1) # left 
    # this runs the dfs with initial value or else the value r,c wont run its ideal just defined 
    dfs(sr,sc)
    return image
# to make the matrix formatiom custom we gave number of rows and column 
rows = int(input("Enter the number of rows :"))
column = int(input("Enter the number of column :"))
# matrix is stored in image variable 
image = []
print("Enter the desired image values :")
# this maps the individual rows of values into each list 
for _ in range(rows):
    row = list(map(int,input().split()))
    # this is optional just to handle the if the value entered is not a square matrix 
    if len(row) != column:
        raise ValueError("The value you have entered is not square matrix".format(column))
    image.append(row)
# the row and column value are given as custom input  
sr = int(input("Enter the desired row index :"))
sc = int(input("Enter the desired column index :"))
# the new value which should be changed is given as custom input
new = int(input("Enter the new value should be filled :"))
# flood fill function is called and the output is printed in 2d view using an loop 
print("Flood Filled image")
f = flood_fill(image,sr,sc,new)
for row in f:
    print(*row)