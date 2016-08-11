#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-11 18:28:44
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://example.org
# @Version : $1.0

# import modules
import xlrd,sys,re,urlhelper

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
					my_file.write(str(text))

# Main method, run $python3 urlExtractorFromXls.py filename.xls
# You can put all the .xls files in the same directory and
# run $python3 urlExtractorFromXls.py *.xls
def main():
	i = 1
	while(i <= len(sys.argv)-1):
		fn = str(sys.argv[i])
		read_and_save(fn)
		i += 1

if __name__ == '__main__':
	main()