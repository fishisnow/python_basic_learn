#coding:utf-8
#网站构造函数
from xml.sax.handler import ContentHandler
from xml.sax import parse
import os


class Dispatcher:

    def dispatch(self, prefix, name, attrs = None):
        #查找合适的处理程序，构造参数元组
        mname = prefix

    def startElement(self, name, attrs):
        self.dispatch('start', name, attrs)

    def endElement(self, name):
        self.dispatch('end', name)




