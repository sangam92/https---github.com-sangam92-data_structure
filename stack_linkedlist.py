class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.head = None

    def push_element(self,data):
        newnode = Node(data)
        if self.head == None:
            print("Stack is empty push")
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def pop_elements(self):
        if self.head == None:
            print("stack is empty")
        else:
            pop_ele = self.head
            self.head.next = self.head
            #self.head = None


    def display(self):
        disp = self.head
        while disp is not None:
            print(disp.data)
            disp = disp.next
        print(disp.data)

s= Stack()

s.push_element(23)
s.push_element(12)
s.push_element(56)


s.pop_elements()

s.display()
