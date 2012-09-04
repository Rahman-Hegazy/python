#!/usr/bin/python2
# coding=utf8

# module for getting the lan ip address of the computer
## http://stackoverflow.com/a/1947766

import os
import socket
import fcntl
import struct
import pdb
import code
import readline
import rlcompleter

#if os.name != "nt":
#
#    import fcntl
#    import struct
#
#    def get_interface_ip(ifname):
#        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#        return socket.inet_ntoa(fcntl.ioctl(
#                        s.fileno(),
#                        0x8915,  # SIOCGIFADDR
#                        struct.pack('256s', ifname[:15])
#                )[20:24])
#
#def get_lan_ip():
#    ip = socket.gethostbyname(socket.gethostname())
#    if ip.startswith("127.") and os.name != "nt":
#        interfaces = ["eth0","eth1","eth2","wlan0","wlan1","wifi0","ath0","ath1","ppp0"]
#        for ifname in interfaces:
#                try:
#                        ip = get_interface_ip(ifname)
#                        break;
#                except IOError:
#                        pass
#    return ip

ifname='eth1'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(),
                        0x8915,  # SIOCGIFADDR
                        struct.pack('256s', ifname[:15])
                )[20:24])

readline.parse_and_bind('tab: complete')
## 默认用 __main__.__dict__ 里边的对象进行补全，而不是 globals()，重新设置 readline 补全函数
readline.set_completer(rlcompleter.Completer(locals()).complete)
code.interact(local=locals(), banner=None)

#pdb.set_trace()
get_lan_ip()


#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect(("gmail.com",80))
#print(s.getsockname()[0])
#s.close()











