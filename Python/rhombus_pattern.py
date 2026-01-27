def rhombus(n):
    mid = n // 2
    for i in range(n):
        space = abs(mid - i)
        stars = n - 2*space
        print(" "*space + "*"*stars)

n = int(input("Enter the total width of Rhombus :"))
rhombus(n)