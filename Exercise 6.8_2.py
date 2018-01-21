# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:33:43 2018

@author: ichangting
"""
'''
The greatest common divisor (GCD) of a and b is the largest number that divides
both of them with no remainder.
One way to find the GCD of two numbers is Euclid’s algorithm, which is based on the observation
that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). 
As a base case, we can use gcd(a, 0) = a.
'''

# Exercise 6.8

def gcd(a,b):
    if b==0:
        return a
    else:
        r=a%b
        gcd(b,r)

a=int(raw_input('a='))
b=int(raw_input('b='))

if a<b:
    t=a
    a=b
    b=t 

print 'a=',a
print 'b=',b

g=gcd(a,b)
print 'The greatest common divisor is',g
