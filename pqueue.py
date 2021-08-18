#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:15:17 2020

@author: sangam
"""

class Priorityqueue:
    def __init__(self):
        self.pqueue=[]
       
       
    def insert(self,dataval):
        self.pqueue.append(dataval)
        
    def remove_priority(self):
        max = 0
        for i in range(len(self.pqueue)):
            if self.pqueue[i]>self.pqueue[max]:
                max=i
        item=self.pqueue[max]
        del self.pqueue[max]
        return item
                
if __name__=="__main__":
    pq=Priorityqueue()
    pq.insert("5")
    pq.insert("2")
    pq.insert("3")
    
    print(pq.pqueue)
    
    pq.remove_priority()
    print(pq.pqueue)
    
    