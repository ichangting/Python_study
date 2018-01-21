# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:26:04 2018

@author: ichangting
"""

# Exercise 6.5
# The Ackermann function, A(m, n)
# A(m, n) =
# n + 1, if m = 0
# A(m - 1, 1) if m > 0 and n = 0
# A(m - 1, A(m, n - 1)) if m > 0 and n > 0.

def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))

m=float(raw_input('m='))
n=float(raw_input('n='))        
result=ack(m,n)
print 'result=',result
