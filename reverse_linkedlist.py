def reverselinkedlist(self):
    curr = self.head
    prev = None
    curr.next = None

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    self.head = prev