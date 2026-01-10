class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insert(root,val):
    if root is None:
        return tree(val)

    if val < root.val:
        root.left = insert(root.left,val)
    else:
        root.right = insert(root.right,val)

    return root

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)

root = tree(8)
root.left = tree(3)
root.right = tree(10)
root.right.right = tree(14)

val = 13

insert(root,val)
print("final path :",end=" ")
inorder(root)
print()