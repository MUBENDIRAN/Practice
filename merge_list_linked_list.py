# add the necessary linked list base to make the complete program 
def merge_list(self,head1,head2):
    # to make the logic simple we create a simple dummy variable as the begining and tail will follow up in back starts from it to monitor
    dummy = Node(0)
    tail = dummy 
    # when head1 and 2 not None they are compared and the least one added to tail.next by the way we add from the end and build the merge list
    while head1 is not None and head2 is not None:
        if head1 < head2:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
    # since the loop finished only one element will be left so we make tail as tail.next 
    tail = tail.next
    # to assume which head has the last element by None condition and fill the last tail.next and return dummy.next where actual merge list start 
    if head1 is not None:
        tail.next = head1
    else:
        tail.next = head2
    return dummy.next
