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


def insert(root,node):
    if root is None:
        root=node
    else:
        if root.val < node:
            root.right=None
            root.right=node
        else:
            if root.left is None:
                root.left=None
                root.left=node
                
       
         