#coding:utf-8
import pymysql
import time

def getMysqlConn():
	#创建连接
	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', 
		passwd='root', db='db_wanghong', charset='utf8')
	return conn
def getNowTime():
	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))