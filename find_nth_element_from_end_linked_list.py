# this class node is used for common object usage across independent functions
class Node:
    def __init__(self,data):
        # this stores the linked list values as object which can be accessed via data (reference)
        self.data = data
        # since this does not have next its None its the final 
        self.next = None
# this independent function converts list to linked list
def build_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head
# this function do three operation find the nth element remove it and make the linked list normal
def remove_nth_element_from_end(head,n):
    # we use dummy node so the head wont be modified dummy.next holds the real head
    dummy = Node(0)
    dummy.next = head
    # we start from dummy so we wont lose the link of the list 
    slow = dummy
    fast = dummy
    # this fast finds the nth element
    for _ in range(n):
        if not fast.next:
            return dummy.next
        fast = fast.next
    # after slow and fast moved on same format when fast reaches end slow will be before the nth element
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    # we replace the nth element by next of next so it will be removed from the link
    slow.next = slow.next.next
    # this return the actual head and the new linked list
    return dummy.next
    # this print the linked list tranversal
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    # this create a new line so when the output is printed new output printed on next line 
    print()

arr = list(map(int,input().split()))
n = int(input())
# this helps in where the chain starts 
head = build_list(arr)
# this helps in if the start changes after deletion update the head to the new first node
head = remove_nth_element_from_end(head,n)
print_list(head)