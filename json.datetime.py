#!/usr/bin/python2
# coding=utf8

## python 的 json 模块知道如何处理list,dict,tuple,string等
## 但无法序列化不知道的类型(如 date,datetime,自定义 object)
## http://my.oschina.net/lanybass/blog/73171

import json
import datetime

class MyClass(object):
    def __init__(self):
        self.a=1
        self.b=2

def _default(obj):
    if isinstance(obj,datetime.datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj,datetime.date):
        return obj.strftime('%Y-%m-%d')
    elif isinstance(obj,MyClass):
        return {'a':obj.a,'b':obj.b}
    else:
        raise TypeError('%r is not JSON serializable' % obj)

my_obj=MyClass()

print json.dumps({'now': datetime.datetime.now(), 'today': datetime.date.today(), 'my_obj': my_obj},default=_default)









