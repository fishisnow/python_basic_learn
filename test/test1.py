#coding:utf-8
import urllib2

html = urllib2.urlopen("http://www.huajiao.com/user/12504837").read()
if html is None: 
print html