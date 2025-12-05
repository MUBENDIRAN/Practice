class CircularQueue:
    def __init__(self,capacity):
        self.arr = [0]*capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.size = 0
    
    def enqueue(self):
        if self.size == self.capacity:
            return
        self.rear = (self.rear + 1) % self.capacity
        if self.front == -1:
            self.front = 0
        self.arr[self.rear] = x
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return
        value = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.front = -1
            self.rear = -1
