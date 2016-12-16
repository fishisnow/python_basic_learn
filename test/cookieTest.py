#coding:utf-8
'''
cookielib的使用
'''
import urllib2
import cookielib

cookie = cookielib.CookieJar()
#创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

opener.open('http://www.baidu.com')
for item in cookie:
	print 'Name=' + item.name
	print 'Value=' + item.value