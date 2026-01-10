# this class defines the structure of tree like child and value
class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
# this function defines the rule of bst left < root < right and search a specific element 
def search(root,x):
    if root is None:
        return False
    if root.val == x:
        return True
    elif x < root.val:
        return search(root.left,x)
    else:
        return search(root.right,x)
# values of root and child are created and constructor created and assign the value 
root = tree(10)
root.left = tree(8)
root.left.left = tree(5)
root.right = tree(25)
# search element is defined 
x= 1
# function called and assigned to f variable 
f = search(root,x)
print("the x is found :",f)