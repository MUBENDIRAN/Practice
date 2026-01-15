class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRU:
    def __init__(self,capacity):
        self.cap = capacity
        self.map = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self,node):
        prev = node.prev
        nxt  = node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self,key):
        if key not in self.map:
            return -1

        node = self.map[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self,key,val):
        if key in self.map:
            self._remove(self.map[key])

        node = Node(key,val)
        self.map[key] = node
        self._insert(node)

        if len(self.map) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]

cap = int(input("Enter the Capacity : "))
cache = LRU(cap)

while True:
    cmd = input("> ").split()
    if cmd[0] == "quit": break
    if cmd[0] == "put": cache.put(int(cmd[1]), int(cmd[2]))
    if cmd[0] == "get": print(cache.get(int(cmd[1])))
        