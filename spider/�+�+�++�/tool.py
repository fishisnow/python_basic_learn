#coding:utf-8

import re

class Tool:

    def __init__(self):
        pass

    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换成\n
    replaceline = re.compile('<tr>|<div>|</div>|</p>')
    #将表格td换成\t
    replaceTD = re.compile('<td>')
    #将段落开头换成 \n 加两个空格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其他标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceline, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n  ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)

        return x.strip()