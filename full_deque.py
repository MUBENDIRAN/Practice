# we used class as there are different functions used for different use cases with same object used across functions
class Deque:
    # A constructor is used to create the front and rear temp. value and declaration of capacity and size is defined 
    def __init__(self,capacity):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.size = 0
    # this function defines whether the function is full or not
    def is_full(self):
        self.size == self.capacity
    # this function defines whether the function is empty or not
    def is_empty(self):
        self.size == 0
    # this functions defines the adding of element to front 
    def push_front(self,x):
        if self.is_full():
            return 
        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.size += 1
            return
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = x
        self.size += 1
        # this function defines the adding of element to rear 
    def push_rear(self,x):
        if self.is_full():
            return
        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.size += 1
            return
        self.front = (self.front + 1 ) % self.capacity
        self.arr[self.front] = x
        self.size += 1
    # this function defines the removal of element from front
    def pop_front(self):
        if self.is_empty():
            return
        value = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.front = -1
            self.rear = -1
    # this function defines the removal of element from rear 
    def pop_rear(self):
        if self.is_empty():
            return
        value = self.arr[self.front]
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.front = -1
            self.rear = -1
    # this functions gets the current front element 
    def get_front(self):
        if self.is_empty():
            return None
        return self.arr[self.front]
    # this functions gets the current rear element
    def get_rear(self):
        if self.is_empty():
            return None
        return self.arr[self.rear]


