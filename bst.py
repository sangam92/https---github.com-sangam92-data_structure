# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 14:03:50 2020

@author: sangam
"""

class Node:
    def __init__(self,val):
        self.right=None
        self.left=None
        self.val=val


def insert(root,val):
    if root is None:
        root=Node(val)
    else:
        if root.val < val:
            root.right=insert(root.right,val)
        else:
            root.left=insert(root.left,val)
    return root

def inorder(root):
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 


   
r = Node(50) 
r = insert(r, 30) 
r = insert(r, 20) 
r = insert(r, 40) 
r = insert(r, 70) 
r = insert(r, 60) 
r = insert(r, 80) 
  
# Print inoder traversal of the BST 
print(inorder(r))                
       
         