#coding:utf-8

import urllib
import urllib2
import cookielib

fileName = 'cookie.txt'
cookie = cookielib.MozillaCookieJar('fileName')
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
post_data = urllib.urlencode({
	
})