# this class defines the structure of tree like child and values 
class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
# this function ensures the identical of root1 and root2 
def is_identical(root1,root2):
    # if both are none with no expections its true 
    if root1 is None and root2 is None:
        return True
    # any one is none before another its not 
    if root1 is None or root2 is None:
        return False
    # values of root also plays a role so its also checked 
    if root1.val != root2.val:
        return False
    # and similarly childs values and strucutre are also checked 
    return(is_identical(root1.left,root2.left)and
    is_identical(root1.right,root2.right))
# values are defined 
root1 = tree(10)
root1.left = tree(5)
root1.right = tree(15)
root2 = tree(10)
root2.left = tree(5)
root2.right = tree(20)
# function called 
i = is_identical(root1,root2)
print("identical = ",i)

