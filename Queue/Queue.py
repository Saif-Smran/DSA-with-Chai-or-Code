class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, value):
        self.items.append(value)
    
    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is empty") 
        else:
            return self.items.pop(0)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())