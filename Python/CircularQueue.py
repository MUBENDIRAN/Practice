# we used class since we used different functions with different use cases 
class CircularQueue:
    # this functions manages the initial pointer setup capacity size decisions
    def __init__(self,capacity):
        self.arr = [0]*capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.size = 0
    # this function enqueue by adding element to first place
    def enqueue(self):
    # if size reaches capacity it ends and return nothing 
        if self.size == self.capacity:
            return
        # if it has space one by one the space is filled upto capacity reaches the size
        self.rear = (self.rear + 1) % self.capacity
        # if still the initial pointer is default it changed to initial array for calculation
        if self.front == -1:
            self.front = 0
        # the given element is added to rear pointer in array and size moved since the space is filled 
        self.arr[self.rear] = x
        self.size += 1
    # we used dequeue since we gonna remove the first element
    def dequeue(self):
        # if there is no element to remove as size is empty or zero it returns nothing
        if self.size == 0:
            return
        # since we need to remember the first value we need to remember the original array so stored in a variable
        value = self.arr[self.front]
        # As like rear front pointer is moved and the first element is removed to reallocated in future 
        self.front = (self.front + 1) % self.capacity
        # then size is reduced than capacity 
        self.size -= 1
        # if again size becomes zero or empty the initial default temp. value assigned to front and rear is again used to reallocate the empty space
        if self.size == 0:
            self.front = -1
            self.rear = -1
    # this function return the first element in the current front
    def front(self):
        return self.arr[self.front]
    # this function returns the last element in the current back (rear)
    def rear(self):
        return self.arr[self.rear]
    # this function is optional but still usefull this check the queue is empty or not
    def isEmpty(self):
        return self.size == 0
    # this function is optional too this checks the queue is full or not 
    def isFull(self):
        return self.size == self.capacity