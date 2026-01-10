class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def valid_bst(root):
    def help(node,low,high):
        if node is None:
            return True

        if not (low < node.val < high):
            return False

        return (help(node.left,low,node.val) and help(node.right,node.val,high))

    return help(root,float('-inf'),float('inf'))

root = tree(10)
root.left = tree(50)
root.right = tree(20)

v = valid_bst(root)
print("Is this bst is valid :",v)
