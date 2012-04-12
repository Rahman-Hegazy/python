#!/usr/bin/python  
# -*- coding:utf-8 -*-   
#支持中文（上面一句）  
#很奇怪，在设定字符编码那句上面如果写上中文，也会出错  
#导入模块  
import string  
import sys  
def main():  
    print 'Input a decimal number: '  
    number = raw_input()  
    #string.atoi('string', base) => int  
    number = string.atoi(number)  
    toTwo(number)  
#自定义函数  
def toTwo(number):  
    twoList=[]  
    p=0  
    while (number > 0):  
        #求除以2的余数   
        twoList.append(number & 1)  
        #print number & 1  
        p += 1  
        #number = number / 2  
        number = number >> 1  
    while (p > 0):  
        #print p  
        p -= 1  
        #print twoList[p]  
        #print(twoList[p],end="")  
        sys.stdout.write(str(twoList[p]));  
if __name__ == "__main__":  
    main()  
#以下是一些系统定义的进制转换函数  
#int(str, base) => str  
#hex(num):  decimal => 'ox....'  
#oct(num):  decimal => '0.....'  
