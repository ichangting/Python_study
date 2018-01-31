# 选择排序
# 时间复杂度 O(n**2)
def selction_sort_v1(lst):
  for i in range(len(lst)):
    min_index=i
    for j in range(i+1,len(lst))
      if lst[j]<lst[min_index]:
        min_index=j
    lst.insert(i,min_index)

def swap(lst,i,j):
  temp=lst[i]
  lst[i]=lst[j]
  lst[j]=temp

def selction_sort_v2(lst):
  for i in range(len(lst))
    min_index=i
    for j in range(i+1,len(lst))
      if lst[j]<lst[min_index]:
        min_index=j
    swap(lst,i,min_index)  
    
# 冒泡排序
# 与选择排序类似，但是每次遍历不止交换一次，每次遍历，将最大的值排在最后。

def swap(lst,i,j):
  temp=lst[i]
  lst[i]=lst[j]
  lst[j]=temp
def bubble_sort(lst):
    top = len(lst) - 1
    is_exchanged = True

    while is_exchanged:
        is_exchanged = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i + 1]:
                is_exchanged = True
                swap(lst, i, i + 1)
            top -= 1

lst = [ 1 , 5 , 2 , 4 , 3 ]
bubble_sort(lst)
print(lst)

      
  
  
  
