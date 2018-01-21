# is_triangle

def is_triangle(a,b,c): # 判断三条线段能否构成三角形
    if a+b<c or a+c<b or b+c<a:
        print 'No'
    else:
        print 'Yes'
        
a=int(raw_input('a='))
b=int(raw_input('b='))
c=int(raw_input('c='))

is_triangle(a,b,c)
