#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:41:51 2020

@author: sangam
"""

class Queue:
    def __init__(self):
        self.queue=[]
        
    
    def insert(self,dataval):
        self.queue.append(dataval)
        
    def remove(self):
        self.queue.pop(0)
        
qu = Queue()

print("Inserting the element in the queue")
qu.insert(6)
qu.insert(8)

print("The elements in the queue are",qu.queue)

print("remove function has been called")

qu.remove()


print("The queue after removing elemnts",qu.queue)
            