#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-14 02:49:44
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://xiax.tech
# @Version : $2.0

# Import Modules
from __future__ import division
import requests,re, os, sys, time, urllib2
from readability import Document
from HTMLParser import HTMLParser
from progressbar import *

reload(sys)  
sys.setdefaultencoding('utf-8')  
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
def feedtheURLs(url, fileNum):
	try:
		if ("sina.com" in url):
			### enocode issue
			response = requests.get(url, timeout=10)
			response.raise_for_status()
		else:
			response = requests.get(url, timeout=10)
			response.raise_for_status()

	except Exception:
		return
	doc = Document(response.text)

	try:
		title = doc.title()
		# content = doc.content()
		summary = doc.summary()
		title = strip_tags(title)
		# content = strip_tags(content)
		summary = strip_tags(summary)
		# print (title)
		# sys.exit()
	except Exception:
		return
		
	with open("Crawler_Output/Articles{}.txt".format(fileNum), "a") as my_file:
		my_file.write("标题:" + title.encode('utf-8'))
		my_file.write("\n链接:" + url)
		my_file.write("文章内容:\n" +summary.encode('utf-8'))

	clean_lines = []
	with open("Crawler_Output/Articles{}.txt".format(fileNum), "r") as f:
		lines = f.readlines()
		clean_lines = [l.strip() for l in lines if l.strip()]

	with open("Crawler_Output/Articles{}.txt".format(fileNum), "w") as f:
# 		f.write('''
# ========================================================
# 			''')
		f.writelines('\n'.join(clean_lines))
		f.write('''
========================================================
			''')

def main():
	counter = 0
	fileNum = 1
	progressCounter = 0
	if not os.path.exists("Crawler_Output"):
		os.makedirs("Crawler_Output")
	with open("Output.txt" , "r") as f:
		lines = f.readlines()
		total = sum(1 for line in open('Output.txt'))
		# [feedtheURLs(l) for l in lines]
		print "There is a totla of {} links".format(total)
		for l in lines:
			feedtheURLs(l, fileNum)
			counter += 1
			progressCounter += 1
			pbar = ProgressBar().start()
			pbar.update(int(progressCounter/(total)*100))
			time.sleep(0.01)
			if (counter>100):
				counter = 0
				fileNum += 1

if __name__ == '__main__':
	main()