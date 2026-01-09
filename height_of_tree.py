class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return -1

    left_h = height(root.left)
    right_h = height(root.right)

    return 1 + max(left_h,right_h)

root = tree(1)
root.left = tree(2)
root.right = tree(3)
root.right.right = tree(4)

h = height(root)
print("height of the tree :",h)