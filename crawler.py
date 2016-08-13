#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-11 18:28:44
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://example.org
# @Version : $1.0
# 
import requests,re
from readability import Document
from HTMLParser import HTMLParser

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

# def removeSpace(text):
# 	pattern = re.compile(r'\s+')
# 	text = re.sub(pattern, '', text)
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
		my_file.write(title.encode('utf8'))
		my_file.write(summary.encode('utf8'))

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