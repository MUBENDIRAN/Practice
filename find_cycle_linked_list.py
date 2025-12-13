
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
def build_list(arr):
    head = Node(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head
def cycle_has(head):
    # if  head and head.next is none how it can be cycle , may be self looped but its advanced not for us 
    if head is  None or head.next is None:
        return False
    # both floyd pointer start from head the initial
    slow = head
    fast = head
    # if fast and fast.next is not none then loop continues
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    # if slow and fast meets after the initial stage while in loop then its a cycle 
        if slow == fast:
            return True

    return False

arr = list(map(int,input().split()))

head = build_list(arr)
print(cycle_has(head))
