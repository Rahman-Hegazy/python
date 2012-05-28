#!/usr/bin/python
# coding:utf8

import httplib
import urllib

httplib.HTTPConnection.debuglevel=1
page=urllib.urlopen("http://douban.com")
print"status:", page.getcode()



