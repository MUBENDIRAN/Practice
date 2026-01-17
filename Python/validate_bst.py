# this class defines the structure of the tree like child and value 
class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
# this checks the binary tree is valid or not we can use inorder too & this follow bst rule left < root < right 
def valid_bst(root):
    # this nested function is not necessary we can directly defines in valid_bst but we need to defines the inf and expose it public so we used nested 
    def help(node,low,high):
        if node is None:
            return True

        if not (low < node.val < high):
            return False

        return (help(node.left,low,node.val) and help(node.right,node.val,high))

    return help(root,float('-inf'),float('inf'))
# values of root and child is created and constructor is runned when created 
root = tree(10)
root.left = tree(50)
root.right = tree(20)
# the valid bst function is runned 
v = valid_bst(root)
print("Is this bst is valid :",v)
