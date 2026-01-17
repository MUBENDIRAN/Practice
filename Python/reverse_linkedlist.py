# this class helps in making the arr elements as linked list objects 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# this makes the element map to linked list object
def built(arr):
    head = Node(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head
# this reverse the linked list
def reverselinkedlist(head):
    # initially the current is self.head and others are None for temp. value
    curr = head
    prev = None
    
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
    return prev
# this function transverse the linked list and print transversely
def print_list(head):
    curr = head
    while curr:
        print(curr.data,end=" ")
        curr = curr.next
    print()

arr = list(map(int,input().split()))
head = built(arr)

ans = reverselinkedlist(head)
print_list(ans)