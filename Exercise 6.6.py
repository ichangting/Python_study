# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:43:12 2018

@author: ichangting
"""

# palindrome.py

def first(word):
    return word[0]
    
def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(s): # 判断回文
    for i in range(l/2):
        if first(s)!=last(s):
            return False
        else:
            s=middle(s)
    return True   

s=str(raw_input('Input a string:'))
l=len(s)

print 'the first letter is:',first(s)
print 'the middle letter is:',middle(s)
print 'the last letter is:',last(s) 

print 'is palindrome?:',is_palindrome(s)
