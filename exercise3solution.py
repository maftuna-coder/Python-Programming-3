# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:01:01 2019

@author: Maftuna
"""

def XOR(a,b,c):
    a = int(a)
    b = int(b)
    c = str("XOR")
    if ((a and not b) or (not a and b))==1:
        return 1
    else:
        return 0
    
def Main():
    a = input("enter value for first input ->  ")
    b = input("enter value for second input ->  ")
    c ='XOR'
    x = XOR(a,b,c)
    print ("Output of {} XOR {} is {}".format(a, b, x))
                  
Main()
      