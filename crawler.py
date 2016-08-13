#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-14 02:49:44
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://xiax.tech
# @Version : $1.0

# Import Modules
import requests,re
from readability import Document
from HTMLParser import HTMLParser

# for stripping html tags
class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)

def strip_tags(text):
	s = MLStripper()
	s.feed(text)
	return s.get_data()

# crawl data with the given url and save it to Crawler_Output.txt
def feedtheURLs(url):
	response = requests.get(url)
	doc = Document(response.text)
	title = doc.title()
	# content = doc.content()
	summary = doc.summary()
	title = strip_tags(title)
	# content = strip_tags(content)
	summary = strip_tags(summary)

	with open("Crawler_Output.txt", "a") as my_file:
		my_file.write("标题:" + title.encode('utf8'))
		my_file.write("\n链接:" + url)
		my_file.write("文章内容:\n" +summary.encode('utf8'))

	clean_lines = []
	with open("Crawler_Output.txt", "r") as f:
		lines = f.readlines()
		clean_lines = [l.strip() for l in lines if l.strip()]

	with open("Crawler_Output.txt", "w") as f:
# 		f.write('''
# ========================================================
# 			''')
		f.writelines('\n'.join(clean_lines))
		f.write('''
========================================================
			''')

def main():
	with open("Output.txt" , "r") as f:
		lines = f.readlines()
		[feedtheURLs(l) for l in lines]

if __name__ == '__main__':
	main()