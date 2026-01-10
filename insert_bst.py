# this class defines the structure of tree like child and value 
class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
# this function enables the inserting of nodes at a perfect place & this also follow bst rule left < root < right 
def insert(root,val):
    if root is None:
        return tree(val)

    if val < root.val:
        root.left = insert(root.left,val)
    else:
        root.right = insert(root.right,val)

    return root
# this function is used to get the tree after the insertion but its sorted you can try some other too 
def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
# values of root and child are created and constructor runs when created 
root = tree(8)
root.left = tree(3)
root.right = tree(10)
root.right.right = tree(14)
# value to be inserted
val = 13
# this runs the insert function 
insert(root,val)
print("final path :",end=" ")
# this runs the inorder function 
inorder(root)
print()