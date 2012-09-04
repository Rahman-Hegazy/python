#!/usr/bin/python2
# coding=utf8

import sys

## print 不换行 即时输出 解决方案
sys.stdout.write('hello world with sys.stdout.flush()')
sys.stdout.flush()

sys.stdout.write('hello world without sys.stdout.flush()')

sys.stdout.write('\nhello world with sys.stdout.write(\'string\' + \'\\n\')' + '\n')



