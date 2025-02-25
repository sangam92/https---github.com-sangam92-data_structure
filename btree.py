#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:56:36 2020

@author: sangam
"""

class Btree:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        
    
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left=Btree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right=Btree(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    
    
    
    
    
    def printtree(self):
        if self.left:
            self.left.printtree()
        print( self.data),
        if self.right:
            self.right.printtree()

node=Btree(10)
node.insert(23)
node.insert(67)

node.printtree()