#coding:utf-8
'''
有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''
cnt = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i!=j and i!=k and j!=k:
                #print 100*i+10*j+k
                cnt += 1
print cnt
