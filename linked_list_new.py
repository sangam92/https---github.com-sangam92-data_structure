class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_start(self,data):

        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def traverse_list(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval.next = self.head
l1 = Linkedlist()
l1.insert_start(3)
l1.insert_start(5)
l1.insert_start(7)
l1.traverse_list()
