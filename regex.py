#!/usr/bin/python2
# coding=utf8

import re

# 通过正则表达式来提取匹配的内容
# [1] 要用()将需要的内容包含起来
# [2] 编号为0的group是整个符合正则表达式的内容，编号为1的是第一个(及对应的)包含的内容
# @param regex: regular expression, use () to group the result
#               正则表达式，用()将要提取的内容包含起来
# @param content:
# @param index: start from 1, depends on the \p regex's ()
#               从1开始，可以通过数(来得到，其中0是全部匹配
# @return: the first match of the \p regex
#          只返回第一次匹配的内容
## http://blog.csdn.net/yiluochenwu/article/details/6894993

def extractData(regex,content,index):
    ret='0'
    pattern=re.compile(regex)
    match_regex=pattern.search(content)
    if match_regex:
        ret=match_regex.group(index)
    return ret

regex=r'hello(.*),hi(.*)'
content='hello world,hi Jimy'

print extractData(regex,content,0)
print extractData(regex,content,1)
print extractData(regex,content,2)

