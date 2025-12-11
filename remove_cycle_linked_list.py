def cycle_remove(self):
    slow = self.head
    fast = self.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast :
            break
    
    if fast is None and fast.next is None:
        return

    slow = self.head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    ptr = slow
    while ptr.next != slow:
        ptr = ptr.next 

    ptr.next = None