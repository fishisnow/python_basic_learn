#coding:utf-8
"""
Urllib库的使用
"""
import urllib2
request = urllib2.Request("http://www.xxxxx.com")
try:
	response = urllib2.urlopen(request)
except urllib2.HTTPError, e:
	if hasattr(e, 'code'):
		print e.code
except urllib2.URLError, e:
	if hasattr(e, 'reason'):
		print e.reason
else:
	print 'ok'
