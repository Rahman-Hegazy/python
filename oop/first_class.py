#!/usr/bin/python2

class Person:
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print("ink")
        print('hello' , self.name)

p = Person('world')

p.sayHi()

