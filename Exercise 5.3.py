# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:07:01 2018

@author: ichangting
"""
# Fermat’s Last Theorem

def check_fermat(a,b,c,n):
    if n>2 and a**n+b**n==c**n:
        print 'Holy smokes, Fermat was wrong!'
    else:
        print 'No, that doesn’t work.'
            
a=int(raw_input('a='))
b=int(raw_input('b='))
c=int(raw_input('c='))
n=int(raw_input('n='))

check_fermat(a,b,c,n)
    
    
