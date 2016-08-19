#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-11 18:28:44
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://xiax.tech
# @Version : $2.0

# import modules
import xlrd,sys,re,urlhelper,os

# Read data from Excel Cells and check if it is an URL
# If so, write it into the Output file
def read_and_save(filename):
	book = xlrd.open_workbook(filename)
	sh = book.sheet_by_index(0)
	with open("Output.txt", "a") as my_file:
		for rx in range(sh.nrows):
			for cx in range(sh.ncols):
				text = str(sh.cell_value(rowx=rx, colx =cx))
				validation = re.findall(urlhelper.URL_REGEX, text)
				if (validation):
					my_file.write(str(text)+"\n")

# Main method, run $python3 urlExtractorFromXls.py filename.xls
# You can put all the .xls files in the same directory and
# run $python3 urlExtractorFromXls.py *.xls
def main():
	i = 1
	while(i <= len(sys.argv)-1):
		fn = str(sys.argv[i])
		read_and_save(fn)
		i += 1
	# if (os.path.isfile("Output.txt")):
	# 	uniqlines = set(open("Output.txt").readlines())
	# 	fill = open("Output.txt", 'w').writelines(set(uniqlines))

	# Solution without messing with order
	# lines_seen = set() # holds lines already seen
	# outfile = open('Output.txt', "w")
	# for line in open('Output.txt', "r"):
	#     if line not in lines_seen: # not a duplicate
	#         outfile.write(line)
	#         lines_seen.add(line)
	# outfile.close()

if __name__ == '__main__':
	main()