class tree:
    def __init__(self,val):
        self.val = val
        self.left =  None
        self.right = None

def lca(root,p,q):
    if root is None:
        return None

    if p < root.val and q < root.val:
        return lca(root.left,p,q)
    elif p > root.val and q > root.val:
        return lca(root.right,p,q)
    else:
        return root

root = tree(20)
root.left = tree(10)
root.left.left = tree(5)
root.left.right = tree(10)
root.right = tree(30)
p= 5
q = 10
l = lca(root,p,q)
print("Lowest commmon ancestor of",p,"and",q,"is :",l.val)