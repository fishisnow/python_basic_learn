#coding:utf-8
#查找文件h1标签并打印
from xml.sax.handler import ContentHandler
from xml.sax import parse


class HeadlineHandler(ContentHandler):

    in_headline = False

    def __init__(self, headlines):
        ContentHandler.__init__(self)
        self.headlines = headlines
        self.data = []

    def startElement(self, name, attrs):
        if name == 'h1':
            self.in_headline = True

    def endElement(self, name):
        if name == 'h1':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False

    def characters(self, content):
        if self.in_headline:
            self.data.append(content)

headlines = []
parse("website.xml", HeadlineHandler(headlines))

print 'the follow h1 elements are found:'
for h in headlines:
    print h


