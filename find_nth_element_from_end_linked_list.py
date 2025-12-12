def remove_nth_element_from_end(self,n):
    dummy = Node(0)
    dummy.next = self.head
    slow = dummy
    fast = dummy

    for _ in range(n):
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next