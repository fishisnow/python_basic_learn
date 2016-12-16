#coding:utf-8
'''
将cookie写入文件
'''
import urllib2
import cookielib
fileName = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(fileName)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)