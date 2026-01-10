class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.isFull():
            raise Exception("Queue is full")
        
        if self.isEmpty():
            self.front = 0
        
        self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = value

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        
        value = self.items[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        return value
    

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)  # This will raise an exception: Queue is full
print(cq.dequeue())  # Output: 10
