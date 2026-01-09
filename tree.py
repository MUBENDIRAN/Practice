class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
            return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)

def preorder(root):
    if root is None:
        return
    print(root.val,end=" ")
    preorder(root.left)
    preorder(root.right)



root = tree(10)
root.left = tree(5)
root.right = tree(15)

inorder(root)
print("inorder")
preorder(root)
print("preorder")
            