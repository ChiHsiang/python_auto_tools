#!/usr/bin/env python
# -*- coding: utf-8 -*-

import difflib
import sys
import pdb

try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception as e:
    print("Error:" + str(e)) 
    print("Useage: diff_print.py filename1 filename2")
    sys.exit() 

def readfile(filename):
    try:
        file_handle = open(filename, 'rb')
        text = file_handle.read().splitlines()
        file_handle.close()
        return text
    except IOError as e:
        print('Read file Error:' + str(error))
        sys.exit()

if textfile1 == "" or textfile2 == "":
    print("Useage: diff_print.py filename1 filename2")
    sys.exit()

text1_lines = list(map(lambda ele: ele.decode(encoding = 'UTF-8'), readfile(textfile1)))
text2_lines = list(map(lambda ele: ele.decode(encoding = 'UTF-8'), readfile(textfile2)))

d = difflib.HtmlDiff()
print(d.make_file(text1_lines, text2_lines))
