#!/usr/bin/env python
# coding:utf-8
import sys


#重定向到标准错误输出
print('Fatal error: invalid input!', file=sys.stdout)

#输出重定向至文件
log_file = open('./mylog.txt', 'a+')
print('Fatal error: invalid input!', file=log_file)
log_file.close()
