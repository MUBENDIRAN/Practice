from collections import deque
class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def levelorder(root):
    if root is None:
        return

    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        print(node.val,end=" ")

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

root = tree(1)
root.left = tree(2)
root.right = tree(3)
root.right.right = tree(4)

levelorder(root)
print("levelorder")

