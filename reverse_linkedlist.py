# before this function need to asign the linked list fundamentals so nodes to make working reverse linked list
def reverselinkedlist(self):
    # initially the current is self.head and others are None for temp. value
    curr = self.head
    prev = None
    curr.next = None
    # if current is not none the loop goes through the nodes one by one
    while curr is not None:
        # this step ensures the node chain does not break by saving the current next values for future current 
        next_node = curr.next
        # we change the current next to previous which is none so the pointer changes towards none
        curr.next = prev
        # we change the prev to current to make it as head node for future nodes
        prev = curr
        # previously stored node is made as current node and the process continue
        curr = next_node
    # this ensure the previous value is the head of other nodes so the chance of error and improper placement of nodes will not happen
    self.head = prev