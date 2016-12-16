#coding:utf-8
#decode 是把其他编码的字符串转换为unicode编码的字符串
#encode 把unicode字符串转换成其他编码的字符串

import re
import urllib
import urllib2
import io
from tool import Tool

class BDTB:

    def __init__(self, baseURL, seeLZ):
        self.baseURL = baseURL
        self.seeLZ = "?see_lz=" + str(seeLZ)
        #文件写入操作对象
        self.file = None
        self.defaultTitle = u"百度贴吧"
        #楼层
        self.floor = 1
        self.tool = Tool()

    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + "&pn=" + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #返回urf-8编码内容
            return response.read().decode("utf-8")
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print "百度贴吧连接失败，原因：", e.reason
                return None

    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?<span.*?>(.*?)</span>', re.S)#re.S 表示多行匹配
        result = re.search(pattern, page)
        if result:
            return result.group(1)
        else:
            return None

    #获取该页面的每一层楼的内容
    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode("utf-8"))
        return contents

    def setFileTitle(self, title):
        if title is not None:
            print title
            self.file = io.open(self.defaultTitle + ".txt", mode="w+", encoding="utf-8")
        else:
            self.file = io.open(self.defaultTitle + ".txt", mode="w+", encoding="utf-8")

    def writeData(self, contents):
        for item in contents:
            floorLine = "\n" + str(self.floor) + u"楼-------------------------------------------------------\n"
            self.file.write(floorLine)
            self.file.write(item.decode("utf-8"))
            self.floor += 1

    def start(self):
        pageNum = self.getPageNum()
        title = self.getTitle()
        self.setFileTitle(title)
        if pageNum is None:
            print "URL失效，请重试"
            return
        try:
            for i in range(1, int(pageNum)+1):
                print "正在写入第" + str(i) + "页数据..."
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        except IOError, e:
            print "写入失败:", e.message
        finally:
            print "写入数据成功"

baseURL = "http://tieba.baidu.com/p/3138733512"
bdtb = BDTB(baseURL, 1)
bdtb.start()