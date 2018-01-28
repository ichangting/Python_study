# 两个元素的交换
def swap(lst,a,b):
    temp=lst[a]
    lst[a]=lst[b]
    lst[b]=temp
    
def swap2(a,b):
    t=a
    a=b
    b=t

li=[10,20,30]
swap(li,0,1)
print li

x=10
y=20
swap2(x,y)
print x,y
