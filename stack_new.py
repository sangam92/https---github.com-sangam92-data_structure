class Stack:

    def __init__(self):
        self.stack = []

    def push_element(self,dataval):
        self.stack.append(dataval)
        return self.stack


    def pop_element(self):
        if len(self.stack) ==0:
            print("Stack is empty")
        else:
            self.stack.pop()
        return self.stack

    def peek_element(self):
        return self.stack[0]

s = Stack()

s.push_element(10)
s.push_element(20)
s.push_element(40)

print(s.pop_element())

print(s.peek_element())
