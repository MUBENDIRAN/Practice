class Deque:
    def __init__(self,capacity):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.size = 0
    
    def is_full(self):
        self.size == self.capacity

    def is_empty(self):
        self.size == 0

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
    
    def push_rear(self,x):
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

    def pop_front(self):
        if self.is_empty():
            return
        value = self.arr[self.front]
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.front = -1
            self.rear = -1

    def pop_rear(self):
        if self.is_empty():
            return
        value = self.arr[self.front]
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.front = -1
            self.rear = -1

    def get_front(self):
        if self.is_empty():
            return None
        return self.arr[self.front]

    def get_rear(self):
        if self.is_empty():
            return None
        return self.arr[self.rear]


