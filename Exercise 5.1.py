# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 09:58:05 2018

@author: ichangting
"""
# 打印一个字符串n次

def print_n(s, n):
    if n <= 0:
        return
    else:
        print s
        print_n(s, n-1)
    
s=raw_input('s=')
n=int(raw_input('n='))

print_n(s,n)
