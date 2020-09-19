class Node:
    def __init__(self,data):
        self.data= data
        self.next= None

class clinkedlist:
    def __init__(self):
        self.head = None

    def insertat(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def traverse(self):
        printval = self.head
        print(printval.data)
        
        while (True):
            printval = printval.next
            print(printval.data)
            if printval == self.head:
                break


        print(printval)

cl = clinkedlist()
cl.insertat(5)
cl.insertat(6)
cl.insertat(10)

cl.traverse()
