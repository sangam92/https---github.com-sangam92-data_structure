#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:51:30 2020

@author: sangam
"""

class Stack:
    def __init__(self):
        self.stack=[]
    
    
    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
        
    def top(self):
        return self.stack[-1]
        

newstack=Stack()

newstack.add("Mon")
newstack.add("Tue")
newstack.add("Wed")

print(newstack.top())