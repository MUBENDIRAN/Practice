# this function holds the pattern printing of rhombus
def rhombus(n):
    # this variable finds the middle element of rhombus width
    mid = n // 2
    for i in range(n):
        a = str(i) # since we can't concantenate the integer we converted to string 
        # to perform perfect rhombus we must define perfect space and star since left and right side space determines the perfect rhombus
        space = abs(mid - i) # we used abs to make the negative value to be absolute
        stars = n - 2*space # we used this formula since we need to find the perfect spaces in both left and right to place the star for perfect rhombus
        print(" "*space + a*stars)

n = int(input("Enter the total width of Rhombus :"))
rhombus(n)