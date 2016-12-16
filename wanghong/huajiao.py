#coding:utf-8

import urllib2
from bs4 import BeautifulSoup
import re
import pymysql
from util import *
#过滤页面的liveId
def filterLiveIds(url):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	liveIds = set()
	for link in soup.find_all('a', href=re.compile("^/l/")):
		if 'href' in link.attrs:
			page = link.attrs['href']
			liveId = re.findall('[0-9]+', page)
			liveIds.add(liveId[0])
	return liveIds
#get userId from live page
def getUserId(liveId):
	html = urllib2.urlopen("http://www.huajiao.com/l/" + str(liveId)).read()
	soup = BeautifulSoup(html, 'html.parser')
	text = soup.title.get_text()
	userId = re.findall('[0-9]+', text)[0]
	return userId

#get user info data form user page
def getUserData(userId):
	try:
		html = urllib2.urlopen("http://www.huajiao.com/user/" + str(userId)).read()
		soup = BeautifulSoup(html, 'html.parser')
		userInfo = soup.find('div', id="userInfo")
		if userInfo is None:
			return 0
		data = dict()
		data['userId'] = userId
		data['avatar'] = userInfo.find('div', {"class":"avatar"}).img.attrs['src']
		#class是python保留字，不能使用
		temp = userInfo.h3.get_text('|', strip=True).split('|')
		print temp[0].encode('utf-8')
		data['userName'] = temp[0]
		data['level'] = temp[1]
		temp = userInfo.find('ul', {"class":"clearfix"}).get_text('|', strip=True).split('|')
		data['follow'] = temp[0]
		data['followed'] =temp[2]
		data['supported'] = temp[4]
		data['experience'] = temp[6]
		print data
		return data
	except AttributeError, e:
		print(str(userId) + ':html parser error in getUserData()')
		return 0
#update user data
def updateUserData(data):
	conn = getMysqlConn()
	cur = conn.cursor()
	sql = 'replace into huajiao_user(userId, userName, level, follow, followed, supported, experience, avatar, scrapedTime)'
	try:
		cur.execute('use db_wanghong')
		cur.execute("set names utf8mb4")
		cur.execute(sql + ' values (%s, %s, %s, %s, %s, %s, %s, %s, %s)', 			
			(data['userId'], data['userName'], int(data['level']), int(data['follow']), int(data['followed']),
				int(data['supported']), int(data['experience']), data['avatar'], getNowTime()))
		conn.commit()

	except pymysql.err.InternalError as e:
		print(e)

#get user lives history
def getUserLives(userId):
     try:
         url = "http://webh.huajiao.com/User/getUserFeeds?fmt=json&amp;uid=" + str(userId)
         html = urlopen(url).read().decode('utf-8')
         jsonData = json.loads(html)
         if jsonData['errno'] != 0:
             print(str(userId) + "error occured in getUserFeeds for: " + jsonData['msg'])
             return 0
         return jsonData['data']['feeds']
     except Exception as e:
         print(e)
         return 0
# update user live data
def replaceUserLive(data):
    conn = getMysqlConn()
    cur = conn.cursor()
    try:
        print(data)
        cur.execute("USE db_wanghong")
        cur.execute("set names utf8mb4")
        cur.execute("REPLACE INTO huajiao_live(liveId,userId,watches,praises,reposts,replies,publishTimestamp,title,image,location,scrapedTime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )", (int(data['relateid']),int(data['FUserId']), int(data['watches']),int(data['praises']),int(data['reposts']),int(data['replies']),int(data['publishtimestamp']),data['title'], data['image'], data['location'],getNowTime())
        )
        conn.commit()
    except pymysql.err.InternalError as e:
        print(e)


url = 'http://www.huajiao.com'
userIds = filterLiveIds(url)
for userId in userIds:
	data = getUserData(userId)
	if data != 0:
		updateUserData(data)