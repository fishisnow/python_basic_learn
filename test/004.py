#coding:utf-8
#判断101-200之间有多少个素数，并输出所有素数

from math import sqrt

cnt  = 0

for i in range(101, 201, 2):
    flag = True
    j = int(sqrt(i))
    for k in range(2, j+1):
        if(i % k == 0):
            flag = False
            break
    if flag:
        print i
        cnt += 1
