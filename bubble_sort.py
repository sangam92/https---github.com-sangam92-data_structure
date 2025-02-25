#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:53:04 2020

@author: sangam
"""

print('This is an implementation of the Bubble Sort Algorithm')

def Bubble_sort(list1):
    for i in list1:
        temp=0
        if list1[i] > list1[i+1]:
            temp=list1[i]
            list1[i]=list1[i+1]
            list1[i+1]=temp
        
            
        
        
        
list1=[1,2,3,1,4,2,6,5,9,8,7]

Bubble_sort(list1)

print(list1)