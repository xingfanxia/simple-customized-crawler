#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-14 02:49:44
# @Last Modified: 2016-08-19 20:31:20
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://xiax.tech
# @Version : $3.0

# Import Modules
from __future__ import division
import requests,re, os, sys, time
from readability import Document
from HTMLParser import HTMLParser
from progressbar import *
from urllib2 import urlopen

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
def feedtheURLs(url, fileName):
	# fuck you sina
	if ("sina" in str(url)):
			content = urlopen(url).read()
			str_start = '<!--博文正文 begin -->'
			str_end = '<!-- 正文结束 -->'
			start = content.find(str_start)
			end = content.find(str_end)
			con1 = '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n'
			con2 = content[start:end]
			body = con1+con2
			doc = Document(body)
	else:
		try:
			response = requests.get(url, timeout=10)
			response.raise_for_status()

		except Exception:
			return
		doc = Document(response.text)

	try:
		# fuck sina
		if ("sina" in str(url)):
			title = str(re.findall("<h2.*?\/h2>", body)[0]).decode('utf-8')
		else:	
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
		
	with open("Crawler_Output/{}.txt".format(fileName), "a") as my_file:
		my_file.write("标题:" + title.encode('utf-8'))
		my_file.write("\n链接:" + url)
		my_file.write("文章内容:\n" +summary.encode('utf-8'))

	clean_lines = []
	with open("Crawler_Output/{}.txt".format(fileName), "r") as f:
		lines = f.readlines()
		clean_lines = [l.strip() for l in lines if l.strip()]

	with open("Crawler_Output/{}.txt".format(fileName), "w") as f:
# 		f.write('''
# ========================================================
# 			''')
		f.writelines('\n'.join(clean_lines))
		f.write('''
========================================================
			''')

def main():
	progressCounter = 0
	if not os.path.exists("Crawler_Output"):
		os.makedirs("Crawler_Output")
	with open("Output.txt" , "r") as f:
		lines = f.readlines()
		total = sum(1 for line in open('Output.txt'))
		# [feedtheURLs(l) for l in lines]
		print "There is roughly a total of {} links".format(total)
		for l in lines:
			if ("origins/" in l):
				fileName = str(l)[7:-5]
			feedtheURLs(l, fileName)
			progressCounter += 1
			pbar = ProgressBar().start()
			pbar.update(int(progressCounter/(total)*100))
			time.sleep(0.01)

if __name__ == '__main__':
	main()