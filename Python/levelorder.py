# sicne its bfs we cant use recursion so iteration and we use queue first in first out
from collections import deque
# this class defines the structure of tree like childs and values 
class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
# this function operated the levelorder rule 
def levelorder(root):
    # this is the base condition to avoid infinite loop 
    if root is None:
        return
    # we define the q as queue
    q = deque()
    # append the root first 
    q.append(root)
    # while q is not empty pull the oldest element and print 
    while q:
        node = q.popleft()
        print(node.val,end=" ")
    # if the node has childs append them and print the oldest like left and right accordingly 
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
# this assignes the values to root and child 
root = tree(1)
root.left = tree(2)
root.right = tree(3)
root.right.right = tree(4)
# calls the function
levelorder(root)
print("levelorder")

