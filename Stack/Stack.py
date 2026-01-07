class stack:
    def __init__(self):
        self.s = []
    
    def length(self):
        return len(self.s)
    
    def isEmpty(self):
        return len(self.s) == 0
    # using insert at 0th index to simulate stack behavior
    def pushf(self, value):
        self.s.insert(0, value)

    def peekf(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            return self.s[0]

    def popf(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            return self.s.pop(0) 
    
    # Using append and pop to simulate stack behavior
    def pushl(self, value):
        self.s.append(value)
    
    def peekl(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            return self.s[-1]
    
    def popl(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            return self.s.pop()

    

# stk = stack()
# stk.push(10)
# stk.push(20)
# stk.push(30)

# print(stk.peek())

# print(stk.pop()) 
# print(stk.pop()) 
# print(stk.pop()) 

stk = stack()

stk.pushl(10)
stk.pushl(20)
stk.pushl(30)

print(stk.peekl())  # 30
print(stk.popl())   # 30
print(stk.popl())   # 20
print(stk.length()) # 1

