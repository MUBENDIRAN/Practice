class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def is_identical(root1,root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.val != root2.val:
        return False

    return(is_identical(root1.left,root2.left)and
    is_identical(root1.right,root2.right))

root1 = tree(10)
root1.left = tree(5)
root1.right = tree(15)
root2 = tree(10)
root2.left = tree(5)
root2.right = tree(20)

i = is_identical(root1,root2)
print("identical = ",i)

