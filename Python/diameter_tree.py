# this class defines the structure of the tree like child and values 
class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
# this function ensures the diameter of the tree
def diameter(root):
    max_dia  = 0
# this function ensures the height of the tree with then moved to diameter
    def height(node):
        # this keyword says to use the variable of diameter
        nonlocal max_dia
        if node is None:
            return -1
    # this addes the nodes of left and right 
        left = height(node.left)
        right = height(node.right)
    # this replace the values as the height of tree updates since diameter is left + right we use plus two 
        max_dia = max(max_dia,left+right+2)
        # this updates the height of the tree of current node 
        return 1 + max(left,right)
    # function returned untill none and finally dia is returned to dia function
    height(root)
    return max_dia
# this defines the values of the root and child
root = tree(10)
root.left = tree(5)
root.right = tree(15)
root.right.right = tree(20)
# function is called for output 
d = diameter(root)

print("Diameter :",d)

