# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:09:54 2018

@author: ichangting
"""

# A number, a, is a power of b if it is divisible by b and a/b is a power of b. 
# Write a function called is_power that takes parameters a and b and returns True if a is a power of b. 
# Note:you will have to think about the base case.

def is_power(a,b):
    i=0 #作为幂次的标志，初始化为0
    while a!=1:
        if a%b!=0:
            return False
        else: 
            a=a/b
            i+=1
    print 'a=','b**',i # 计算幂次
    return True

a=float(raw_input('a='))
b=float(raw_input('b='))

print is_power(a,b)
    
        
    
