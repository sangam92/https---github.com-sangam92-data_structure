#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:39:31 2020

@author: sangam
"""

class Dlinkedlist:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    def printdata(self):
        print(self.data)


    def insert_linked(self,newval):
        newnode=Dlinkedlist(newval)
        
        


node=Dlinkedlist(10)
node.printdata()
