# this class defines the structure of the tree like child and value 
class tree:
    def __init__(self,val):
        self.val = val
        self.left =  None
        self.right = None
# this function finds the lowest common ancestor of the given values p and q 
def lca(root,p,q):
    if root is None:
        return None

    if p < root.val and q < root.val:
        return lca(root.left,p,q)
    elif p > root.val and q > root.val:
        return lca(root.right,p,q)
    else:
        return root
# the values of root and child is created and constructor is runned 
root = tree(20)
root.left = tree(10)
root.left.left = tree(5)
root.left.right = tree(10)
root.right = tree(30)
#p and q values are defined 
p = 5
q = 10
# the function lca is runned and assigned to l and the value is printed 
l = lca(root,p,q)
print("Lowest commmon ancestor of",p,"and",q,"is :",l.val)