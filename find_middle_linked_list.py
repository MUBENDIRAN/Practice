# the linked list basis must be implemented as per need for proper function of this program
def middlelist(self):
    # if the head is none no middle element so none
    if self.head is None:
        return None
    # we use floyd two pointer both made initial to head for starting 
    slow = self.head
    fast = self.head
    # if fast and fast.next has value then loop continues
    while fast is not None and fast.next is not None:
        # slow means goes slow 1/2 speed of fast and fast is to move fast and find the reach
        slow = slow.next
        fast = fast.next.next
    # if fast reached the end the slow would be in the middle so return slow for middle value
    return slow