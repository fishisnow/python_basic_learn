#coding:utf-8
import urllib2
import urllib
import re


#糗事百科爬虫类

class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        self.headers = {'User-Agent':self.user_agent}
        self.stories = [] #存放每一页的段子
        self.enable = False  #判断程序是否继续运行的变量

    def getPage(self, pageIndex):
        try:
            url = "http://www.qiushibaike.com/hot/page/" + str(pageIndex)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            return content
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print e.code
            elif hasattr(e, 'reason'):
                print "连接糗事百科失败，原因是：", e.reason
                return None

    #返回不带图片的段子列表
    def getPageItems(self, pageIndex):
        content = self.getPage(pageIndex)
        if not content:
            print "页面加载失败..."
            return None
        pattern = re.compile('<div.*?clearfix">.*?<h2>(.*?)</h2.*?' +
                             '<div.*?content">(.*?)</div>(.*?)<div class="stats.*?number">(.*?)</i>', re.S)
        items = re.findall(pattern, content)
        pageStories = []
        for item in items:
            haveImg = re.search("img", item[2])
            if not haveImg:
                pageStories.append([item[0].strip(), item[1].strip(), item[2].strip(), item[3].strip()])
        return pageStories

    #加载页面并提取内容，放到列表中
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    #调用该方法，每次都得到一个段子
    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input  = raw_input()
            self.loadPage()
            if input is 'Q':
                self.enable = False
                return
            else:
                print u"第%d页\t发言人：%s\t内容：%s\t评论数：%s" % (page, story[0], story[1], story[3])

    def start(self):
        print "正在阅读糗事百科，按回车读下一条，按Q退出"
        nowPage = 0
        self.enable = True
        self.loadPage()
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                del self.stories[0]
                nowPage += 1
                self.getOneStory(pageStories, nowPage)

spider = QSBK()
spider.start()




