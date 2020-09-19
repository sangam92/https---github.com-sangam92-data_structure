class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Dlinkedlist:
    def __init__(self):
        self.head = None

    def insert_start(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            newnode.prev = None
            self.head.prev = newnode
            self.head= newnode


    def traverse(self):
        printval = self.head
        while printval.next is not None:
            print(printval.data)
            printval = printval.next
        print(printval.data)

        while printval.prev is not None:
            print(printval.data)
            printval = printval.prev
        print(printval.data)

dl = Dlinkedlist()

dl.insert_start(10)
dl.insert_start(15)
dl.insert_start(20)

dl.traverse()
