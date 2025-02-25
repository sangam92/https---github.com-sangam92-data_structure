class Node:

  def __init__(self,data):
    self.data = data
    self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None
        self.numofnodes = 0

    def insert_start(self,data):
        self.numofnodes = self.numofnodes + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node

        else:
            new_node.nextNode = self.head
            self.head  = new_node

     def insert_end(self,data):
         self.numofnodes = self.numofnodes + 1
         new_node = Node(data)

         actual_node = self.head

         while actual_node.nextNode is not None:
             actual_node =  actual_node.nextNode

        actual_node.nextNode = new_node

        
