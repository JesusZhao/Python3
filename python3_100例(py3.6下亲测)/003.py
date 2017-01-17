#!E:\virtualenv\venv\Scripts\python.exe
# -*- coding:utf-8 -*-
'''
【程序3】
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
程序分析：在10万以内判断，先将该数i加上100后再开方后记录在x中，再将该数i加上268后再开方后记录在y中，如果开方后
　　　　　的结果满足：x * x == i + 100 并且 y * y == i + 268，即是所求。
'''
import math

for i in range(100000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+268))
    if (x * x == i + 100) and (y * y == i + 268):
        print(i)
print('Done.')
