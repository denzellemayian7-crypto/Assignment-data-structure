b. Stack (Linear – LIFO)
Code : 
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def display(self):
        print(self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.display()class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def display(self):
        print(self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.display()

