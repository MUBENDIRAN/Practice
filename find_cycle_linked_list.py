def cycle_has(self):
    if self.head is not None and self.head.next is not None:
        return False

    slow = self.head
    fast = self.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False