class Node:
    def __init__(self,data):
        self.data = data
        self.head = None

    def insert_at_begining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node