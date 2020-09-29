class Queue:

  def __init__(self):
      self.stack = []

  def push_ele(self,data):
      self.stack.append(data)

  def pop_ele(self):
      self.stack.pop(0)

  def display(self):
      print(self.stack)

q = Queue()

q.push_ele(12)
q.push_ele(34)
q.push_ele(01)

q.display()

q.pop_ele()

q.display()
