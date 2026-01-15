# this defines the initial values like key value and previous and next
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
# this class defines the LRU essentials like capacity , map and head and tail for doubly linked list 
class LRU:
    def __init__(self,capacity):
        self.cap = capacity
        self.map = {}
        # we used dummy node values to handle null and edge cases 
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    # this function holds the remove operation of linked list 
    def _remove(self,node):
        prev = node.prev
        nxt  = node.next
        prev.next = nxt
        nxt.prev = prev
    # this function holds the insertion operation of linked list
    def _insert(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    # this function gets the key value if available else return -1 
    def get(self,key):
        if key not in self.map:
            return -1
        # this part removes the got value and insert at first since it becomes Most recent used MCU
        node = self.map[key]
        self._remove(node)
        self._insert(node)
        return node.val
    # this function adds the node with key and value if already available that is removed and newly added 
    def put(self,key,val):
        if key in self.map:
            self._remove(self.map[key])
        # the value is assigned and node and then to map = {} and then inserted 
        node = Node(key,val)
        self.map[key] = node
        self._insert(node)
        # if the length of map is reached the cache is full so the LRU is removed and the cache is maintained optimised 
        if len(self.map) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key] # it completely deletes the LRU 
# custom input 
cap = int(input("Enter the Capacity : "))
cache = LRU(cap)
# this created a infinite loop 
while True:
    cmd = input("> ").split() # this map the input value with split() 
    if cmd[0] == "quit": break # if first word is quit the loop finish 
    if cmd[0] == "put": cache.put(int(cmd[1]), int(cmd[2])) # if put it takes the two values and run the LRU function with that values
    if cmd[0] == "get": print(cache.get(int(cmd[1]))) # similar to put the get also works 
        