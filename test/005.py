#coding:utf-8
#打印所有水仙花数

for i in range(100, 1000):
    a = i/100
    b = (i - a*100)/10
    c = i - a*100 - b*10
    if i == a*a*a + b*b*b + c*c*c:
        print i