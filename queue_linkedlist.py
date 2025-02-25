class Node:

  def __init__(self,data):
    self.data =data
    self.next = None



class Queue:

  def __init__(self):
      self.head = None

  def push_ele(self,data):
      newnode = Node(data)
      if self.head = None:
          self.head = newnode
      else:
          newnode.next = self.head
          self.head = newnode

    
