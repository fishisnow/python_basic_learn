#coding:utf-8
#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数

line = raw_input("please enter a line:")
letter = 0 #中英文字母
space = 0
digit = 0
other = 0

for c in line:
    if c.isalpha():
        letter += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        other += 1

print "line:%d, space:%d, digit:%d, other:%d" % (letter, space, digit, other)

