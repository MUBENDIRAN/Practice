class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def diameter(root):
    max_dia  = 0

    def height(node):
        nonlocal max_dia
        if node is None:
            return -1

        left = height(node.left)
        right = height(node.right)

        max_dia = max(max_dia,left+right+2)
        return 1 + max(left,right)

    height(root)
    return max_dia


root = tree(10)
root.left = tree(5)
root.right = tree(15)
root.right.right = tree(20)
d = diameter(root)

print("Diameter :",d)

