class Node:
    def __init__(self,data):
        self.data = data
        self.head = None

    def insert_at_begining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

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

    def search(self,value):
        curr = self.head

        while curr is not None:
            if curr == value:
                return True
            curr = curr.next
        return False

    def print_value(self):
        curr = self.head
        while curr is not None:
            print(curr.data,end="")
        curr = curr.next


        