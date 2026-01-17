# the linked list basis must be implemented as per need for proper function of this program
def cycle_remove(self):
    slow = self.head
    fast = self.head
    # if fast and fast.next has value loop runs and when the meet each other it breaks 
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast :
            break
    # if fast and fast.next becomes None its not cycle so return nothing no operation
    if fast is None and fast.next is None:
        return
    ''' if its a cycle the slow is pointed towards the head and both slow and fast move one by one from their place when they get equal 
     that place is the correct place to disconnect the cycle its the starting point of cycle '''
    slow = self.head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    ''' after finding the starting point from that next to next the loop moves and again when its reaches the starting point again that is 
    the final point of the cycle after that all made None to remove the cycle '''
    ptr = slow
    while ptr.next != slow:
        ptr = ptr.next 

    ptr.next = None