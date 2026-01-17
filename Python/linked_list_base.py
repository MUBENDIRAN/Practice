class Node:
    # This is the constructor node where data to other nodes is driven and it is the head node so no heading node 
    def __init__(self,data):
        self.data = data
        self.head = None
    # this function helps us to add nodes which are new at the begining of the linked list
    def insert_at_begining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    # this function helps us to add nodes which are new at the end of the linked list
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
    '''this function helps to delete the specific node which is equals to value assigned ,it deleted the value by Bypassing the node so 
     its gets unlinked from list and get deleted if not found job done was None '''
    def delete_value(self,value):
        if self.head is None:
            return

        if self.head == value:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next is not None and curr.next != value:
            curr = curr.next

        if curr.next is None:
            return
        curr.next = curr.next.next
    # this function helps to find a specific node with the specific value assigned if not available action done is nil
    def search(self,value):
        curr = self.head

        while curr is not None:
            if curr == value:
                return True
            curr = curr.next
        return False
    # this function helps to print all nodes in order 
    def print_value(self):
        curr = self.head
        while curr is not None:
            print(curr.data,end="")
        curr = curr.next


        