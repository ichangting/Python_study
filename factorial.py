# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:59:42 2018

@author: ichangting
"""
# 计算阶乘
def factorial(n):
    if n==0:
        return 1
    else:
        recurse=factorial(n-1)
        result=n*recurse
        return result
        
n=int(raw_input('n='))
r=factorial(n)
print 'n!=',r    
