class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def build_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for x in arr[1:0]:
        curr.next = arr(x)
        curr = curr.next
    return head

def remove_nth_element_from_end(head,n):
    dummy = Node(0)
    dummy.next = head
    slow = dummy
    fast = dummy

    for _ in range(n):
        if not fast.next:
            return dummy.next
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next

def print_list(self):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()

arr = list(map(int,input().split()))
n = int(input())

head = build_list(arr)
head = remove_nth_element_from_end(head,n)
print_list(self)