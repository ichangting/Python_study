# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 17:08:37 2018

@author: ichangting
"""
'''
def printCalendar():
    readInput()
    printMonth()
'''

# 判断某一年的某月第一天是星期几
def is_leap_year(year): # 判断闰年,该函数确认正确
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False

def get_num_of_days_in_month(year,month): # 某年的某月一共有多少天，该函数正确
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28

def get_total_num_of_day(year,month):
    days=0 
    for y in range(1900,year):
        if is_leap_year(y):
            days+=366
        else:
            days+=365
    for m in range(1,month):
        days += get_num_of_days_in_month(year,m)
    return days

def get_start_day(year,month):
    return (1+get_total_num_of_day(year,month))%7

q=raw_input('Quit?')
while q !='q':
    y=int(raw_input('year:'))
    m=int(raw_input('month:'))
    print is_leap_year(y)
    print get_num_of_days_in_month(y,m)
    print get_total_num_of_day(y,m)
    print get_start_day(y,m)
