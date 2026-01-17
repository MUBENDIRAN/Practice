# this class defines the structure of tree like childs and value
class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
# this function calculate the height of tree in edges if you need nodes make the base case to 0 
def height(root):
    if root is None:
        return -1 # zero for nodes calculation
# this holds the edge values of left and right side since recursion basically acts as counter the count is added 
    left_h = height(root.left)
    right_h = height(root.right)
    # we add puls one to add with root so the height value is right enough at last 
    return 1 + max(left_h,right_h)
# the root and child values are defined
root = tree(1)
root.left = tree(2)
root.right = tree(3)
root.right.right = tree(4)
# function called 
h = height(root)
print("height of the tree :",h)