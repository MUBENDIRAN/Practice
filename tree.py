# this defines the structure of tree like left and right childs and values of nodes
class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
# this function follows the inorder traversal rule like left - root - right
def inorder(root):
    if root is None:
            return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
# this function follows the preorder traversal rule like root - left - right
def preorder(root):
    if root is None:
        return
    print(root.val,end=" ")
    preorder(root.left)
    preorder(root.right)
# this function follows the postorder traversal rule like left - right - root
def postorder(root):
    if root is None:
        return
    preorder(root.left)
    preorder(root.right)
    print(root.val,end=" ")
# define the values of the root and child
root = tree(10)
root.left = tree(5)
root.right = tree(15)
# calling the functions 
inorder(root)
print("inorder")
preorder(root)
print("preorder")
postorder(root)
print("postorder")
            