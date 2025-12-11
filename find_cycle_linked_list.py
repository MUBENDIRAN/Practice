# the linked list basis must be implemented as per need for proper function of this program
def cycle_has(self):
    # if  head and head.next is none how it can be cycle , may be self looped but its advanced not for us 
    if self.head is not None and self.head.next is not None:
        return False
    # both floyd pointer start from head the initial
    slow = self.head
    fast = self.head
    # if fast and fast.next is not none then loop continues
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    # if slow and fast meets after the initial stage while in loop then its a cycle 
        if slow == fast:
            return True

    return False