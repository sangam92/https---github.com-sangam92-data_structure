"""
Max depth Binary Tree

"""
class Node:
    def __init__(self,data=0):
        self.left=None
        self.right=None
        self.data=data


    def maxDepth(root):
    stack=[root]
    #print("starting",stac)
    res=[]
    count=1
    while stack:
        node=stack.pop()
  
        res.append(node.data)
        count=count+1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return count