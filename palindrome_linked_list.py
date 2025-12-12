# add the necessary linked list base to make the complete program 
def is_palindrome(self):
    # if the initial head and head.next is None then no problem exist so to check we use this condition
    if self.head is not None or self.head.next is not None:
        return True
    # floyd algorithm with its two pointer
    slow = self.head
    fast = self.head
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
        curr = next_node
    # since self.head is the first element in the left we use prev which is the initial element which is reversed used as right side
    left = self.head
    right = prev
    # while we have the right element loop runs and compare with left if equal next check else return false 
    while right is not None:
        if left.data != right.data:
            return False

        left = left.next
        right = right.next
    
    return True


