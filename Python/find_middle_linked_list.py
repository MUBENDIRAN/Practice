# this class helps in providing the linked list element as object to independent function
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# this function ensure to make array element as linked list 
def build_list(arr):
    head = Node(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = Node(x)
        curr = curr.next
    return head
# this function find the middle element of the linked list
def middlelist(head):
    # if the head is none no middle element so none
    if head is None:
        return None
    # we use floyd two pointer both made initial to head for starting 
    slow = head
    fast = head
    # if fast and fast.next has value then loop continues
    while fast is not None and fast.next is not None:
        # slow means goes slow 1/2 speed of fast and fast is to move fast and find the reach
        slow = slow.next
        fast = fast.next.next
    # if fast reached the end the slow would be in the middle so return slow for middle value
    return slow


arr = list(map(int,input().split()))   
# this holds the real head so no changes happens to head  
head = build_list(arr)
ans = middlelist(head)
print(ans.data)