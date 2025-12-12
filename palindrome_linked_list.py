def is_palindrome(self):
    if self.head is not None or self.head.next is not None:
        return True

    slow = self.head
    fast = self.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow

    while curr is not None:
        next_curr = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    left = self.head
    right = prev

    while right is not None:
        if left.data != right.data:
            return False

        left = left.next
        right = right.next
    
    return True


