#!/usr/bin/python2
# coding=utf8

import sys

file='/tmp/fail.ip.txt'

while True:
    line=file.readline()
    ip=line.split(' ')[0]
    print ip
    if not line: break

file.close()




























