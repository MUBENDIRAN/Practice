class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def search(root,x):
    if root is None:
        return False

    if root.val == x:
        return True
    elif x < root.val:
        return search(root.left,x)
    else:
        return search(root.right,x)

root = tree(10)
root.left = tree(8)
root.left.left = tree(5)
root.right = tree(25)
x= 1
f = search(root,x)
print("the x is found :",f)