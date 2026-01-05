class Node:
    def __init__(self, info,next = None):
        self.data = info
        self.next = next


class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def insertAtEnd(self,value):
        temp = Node(value)
        if (self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
    
    def insertAtBeg(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAtMid(self,value,x):
        temp = Node(value)
        t1 = self.head
        while(t1 != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next

    def deleteLL(self,val):
        t1 = self.head
        prev = t1

        if(t1.data == val):
            self.head = t1.next
            return

        while(t1.next != None):
            if(t1.data == val):
                prev.next = t1.next
                return
            else:    
                prev = t1
                t1 = t1.next
        
        if(t1.data == val):
            prev.next = None

    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)


obj = SinglyLinkedList()

obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertAtMid(40,20)
obj.deleteLL(20)
obj.printLL()