#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:21:55 2020

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
    
    def remove(self):
        if len(self.stack) ==0:
            print("The stack has not been created")
        else:
            self.stack.pop()
            print(self.stack)
        

newstack=Stack()

newstack.add("Mon")
newstack.add("Tue")
newstack.add("Wed")

newstack.remove()

