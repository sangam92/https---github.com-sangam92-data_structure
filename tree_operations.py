"""
Tree Traversal and Operations

"""

class Node:
    def __init__(self,data=0):
        self.left=None
        self.right=None
        self.data=data

def display_tree(self):
        if self.left:
            self.left.display_tree()
        print(self.data)
        if self.right:
            self.right.display_tree()


def preorder_iterative(root):
    stack=[root]
    #print("starting",stac)
    res=[]
    while stack:
        node=stack.pop()
  
        res.append(node.data)
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res

def inorder_recursive(root):
    if root is None:
        return []
    return inorder_recursive(root.left)+[root.data]+inorder_recursive(root.right)





def inorder_iterative(root):
    stack=[]
    res=[]
    while stack!=[] or  root is not None:
        while root is not None:
            stack.append(root)
            root=root.left
        root=stack.pop()
        res.append(root.data)
        root=root.right

    return res




    def insert(self,data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif self.data <data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)



def postorder_recursion(root):
    if root is None:
        return []
    return postorder_recursion(root.left) + postorder_recursion(root.right) + [root.data]


n=Node(10)

stack=[]
res=[]
"""
def postorder_iterative(root):
    stack=[10,5,10,2
    res=[]

    while stack!=[] or root is not None:
        while root is not None:
            stack.append(root)
            root = root.left
        root=root.right
        root=stack.pop()
        res.append(root)
"""

n=Node(10)
n.left=Node(5)
n.right=Node(7)
n.left.right=Node(2)

#root.display_tree()   
#print(preorder_iterative(n))

print(inorder_iterative(n))

print(postorder_recursion(n))



