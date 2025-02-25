## detecting the loop in the linked list

class Node:
    def __init__(self,data):
        self.data= data
        self.next = None


class Looplinkedlist:

    def __init__(self):
        self.head = None

    def insert_ele(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode =Node(data)
            newnode.next = self.head
            self.head = newnode

    def print_ele(self):
        element = self.head
        if element is None:
            print("The linked list is empty")
        else:
            while(element):
                print(element.data)
                element = element.next

    def detect_loop(self):
        s_pointer= self.head
        f_pointer = self.head
        while (s_pointer and f_pointer and f_pointer.next):
            s_pointer = s_pointer.next
            f_pointer = f_pointer.next

            if s_pointer == f_pointer:
                return 
