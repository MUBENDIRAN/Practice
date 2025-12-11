def merge_list(self,head1,head2):
    dummy = Node(0)
    tail = dummy 

    while head1 is not None and head2 is not None:
        if head1 < head2:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

    tail = tail.next

    if head1 is not None:
        tail.next = head1
    else:
        tail.next = head2
    return dummy.next
