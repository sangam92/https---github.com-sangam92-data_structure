#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:27:05 2020

@author: sangam
"""

#Reverse the array


def reverse_array(list1):
    array_new=[]
    for i in range(len(list1)-1,-1,-1):
        array_new.append(list1[i])
    return array_new
        
    
    
    
    
    

if __name__=="__main__":
    print("please input the array")
    array_list=input()
    
    array_map=list(map(int,array_list.split(' ')))
    #array_map=[int(i) for i in array_list.split()]
    
    res=reverse_array(array_map)
    print(res)