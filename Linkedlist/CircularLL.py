class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularSLL:
    def __init__(self):
        self.head = None
        self.last = None

    def insertAtEnd(self, value):
        temp = SLLNode(value)

        if self.head is None:
            self.head = self.last = temp
            temp.next = temp
            return

        temp.next = self.head
        self.last.next = temp
        self.last = temp

    def insertAtBeg(self, value):
        temp = SLLNode(value)

        if self.head is None:
            self.head = self.last = temp
            temp.next = temp
            return

        temp.next = self.head
        self.last.next = temp
        self.head = temp

    def insertAtMid(self, value, x):
        if self.head is None:
            return

        t = self.head
        while True:
            if t.data == x:
                temp = SLLNode(value)
                temp.next = t.next
                t.next = temp
                if t == self.last:
                    self.last = temp
                return
            t = t.next
            if t == self.head:
                break

    def deleteCLL(self, val):
        if self.head is None:
            return

        if self.head.data == val:
            if self.head == self.last:
                self.head = self.last = None
                return
            self.last.next = self.head.next
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr != self.head:
            if curr.data == val:
                prev.next = curr.next
                if curr == self.last:
                    self.last = prev
                return
            prev = curr
            curr = curr.next

    def printCLL(self):
        if self.head is None:
            return
        t = self.head
        while True:
            print(t.data)
            t = t.next
            if t == self.head:
                break

class CircularDLL:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        temp = DLLNode(value)

        if self.head is None:
            temp.next = temp.prev = temp
            self.head = temp
            return

        last = self.head.prev
        temp.next = self.head
        temp.prev = last
        last.next = temp
        self.head.prev = temp

    def insertAtBeg(self, value):
        self.insertAtEnd(value)
        self.head = self.head.prev

    def insertAtMid(self, value, x):
        if self.head is None:
            return

        t = self.head
        while True:
            if t.data == x:
                temp = DLLNode(value)
                temp.next = t.next
                temp.prev = t
                t.next.prev = temp
                t.next = temp
                return
            t = t.next
            if t == self.head:
                break

    def deleteCDLL(self, val):
        if self.head is None:
            return

        t = self.head
        while True:
            if t.data == val:
                if t.next == t:
                    self.head = None
                    return
                t.prev.next = t.next
                t.next.prev = t.prev
                if t == self.head:
                    self.head = t.next
                return
            t = t.next
            if t == self.head:
                break

    def printCDLL(self):
        if self.head is None:
            return
        t = self.head
        while True:
            print(t.data)
            t = t.next
            if t == self.head:
                break


