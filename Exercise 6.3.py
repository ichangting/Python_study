# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:45:59 2018

@author: ichangting
"""

# Exercise 6.3
# Write a function is_between(x, y, z) that returns True if x <= y <= z 
# or False otherwise.

def is_between(x,y,z):
    if x<=y and y<=z:
        return True
    else:
        return False

x=int(raw_input('x='))
y=int(raw_input('y='))
z=int(raw_input('z='))

r=is_between(x,y,z)

if r:
    print 'x<=y<=z'
else:
    print 'No'
