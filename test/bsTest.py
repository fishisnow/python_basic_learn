#coding:utf-8
import bs4
from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, "html.parser")

# print soup.prettify()

# print soup.a
# print type(soup.a)

# print soup.p.attrs

# print soup.p['class']

# soup.p['class'] = 'newTitle'
# print soup.p.get('class')

# print soup.p.string

# print type(soup.name)
# print soup.name
# print soup.attrs

# if type(soup.a.string)==bs4.element.Comment:
# 	print soup.a.string
# 	print type(soup.a.string)

# print soup.head.contents

# for child in soup.body.children:
# 	print child

for child in soup.descendants:
	print child