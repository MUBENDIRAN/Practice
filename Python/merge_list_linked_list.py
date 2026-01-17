# this class helps in making nodes of arr element in linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# this created the arr1 elements into linked list
def build1(arr1):
    head1 = Node(arr1[0])
    curr = head1
    for x in arr1[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head1
# this created the arr2 elements into linked list
def build2(arr2):
    head2 = Node(arr2[0])
    curr = head2
    for x in arr2[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head2
# this merge the linked list in sorted order which is already sorted
def merge_list(head1,head2):
    # to make the logic simple we create a simple dummy variable as the begining and tail will follow up in back starts from it to monitor
    dummy = Node(0)
    tail = dummy 
    # when head1 and 2 not None they are compared and the least one added to tail.next by the way we add from the end and build the merge list
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
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

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
head1 = build1(arr1)
head2 = build2(arr2)
ans = merge_list(head1,head2)
curr = ans
while curr:
    print(curr.data,end=" ")
    curr = curr.next
print()

