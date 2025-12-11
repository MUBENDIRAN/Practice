def merge_list(self,head1,head2):
    dummy = Node(0)
    tail = dummy 

    while head1 is not None and head2 is not None:
        if head1 < head2:
            tail = head1
            tail = tail.next
        else:
            tail = head2
            tail = tail.next

    tail = tail.next

    if head1 is not None:
        tail.next = head1
    else:
        tail.next = head2