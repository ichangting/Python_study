# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:13:33 2018

@author: ichangting
"""

# fibonacci
# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    if not isinstance(n, int): # 判断n是否为整数
        print 'Factorial is only defined for integers.'
        return None
    elif n < 0: # 判断n是否为正数
        print 'Factorial is not defined for negative integers.'
        return None
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        
n=int(raw_input('n='))

for i in range(n):
    print fibonacci(i),
