class infix_prefix:

  def __init__(self):
      self.stack = []
      self.output = []
      self.precedence ={'+':1, '-':1, '*':2, '/':2, '^':3} 

  def push_ele(self,ele):
      self.stack.append(ele)
  def pop_ele(self):
      self.stack.pop()

  def inf_pfx(self,expr):
      for i in expr:
          if self.isoperand(i):
              self.output.append(i)

          elif i == '(':
              self.push(i)
