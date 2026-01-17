# this class map the arr element to object and make a linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# this created the arr element to linked list
def build(arr):
    head = Node(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head
# this checks whether it is palindrome or not
def is_palindrome(head):
    # if the initial head and head.next is None then no problem exist so to check we use this condition
    if head is  None or head.next is  None:
        return None
    # floyd algorithm with its two pointer
    slow = head
    fast = head
    # This loop finds the middle element
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    # since slow is the middle element we reverse there and use prev to reverse at point to head prev with initial None
    prev = None
    curr = slow
    # This loop helps in reverse from the middle for comparison
    while curr is not None:
        next_curr = curr.next
        curr.next = prev
        prev = curr
        curr = next_curr
    # since self.head is the first element in the left we use prev which is the initial element which is reversed used as right side
    left = head
    right = prev
    # while we have the right element loop runs and compare with left if equal next check else return false 
    while right is not None:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next
    
    return True

arr = list(map(int,input().split()))
head = build(arr)
print(is_palindrome(head))

