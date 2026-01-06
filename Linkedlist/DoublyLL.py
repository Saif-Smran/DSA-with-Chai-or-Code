class Node:
    def __init__(self, info=None, prev=None, next=None):
        self.data = info
        self.prev = prev
        self.next = next
    
class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)

        if(self.head == None):
            self.head = temp
            return
        
        t = self.head
        while(t.next != None):
            t = t.next
        
        t.next = temp
        temp.prev = t
    
    def insertAtbeg(self, value):
        temp = Node(value)

        if(self.head == None):
            self.head = temp
            return
        
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insertAtMid(self, value, x):
        temp = Node(value)
        t = self.head

        while(t != None):
            if(t.data == x):
                break
            t = t.next
        
        temp.next = t.next
        temp.prev = t
        t.next.prev = temp
        t.next = temp

    def deleteDLL(self, val):
        if(self.head == None):
            print("Linked List is empty")
            return

        t = self.head
        if(t.data == val):
            self.head = t.next
            self.head.prev = None
            return

        while(t.next != None):
            if(t.data == val):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            t = t.next
        
        if(t.data == val):
            t.prev.next = None
            return

    def printDLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data, end=" <---> ")
            t1 = t1.next
        print(t1.data)
    


obj = DoublyLinkedList()

obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtbeg(5)
obj.insertAtMid(25,20)
obj.deleteDLL(40)

obj.printDLL()