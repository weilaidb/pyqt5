#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
import sys
import types



class Student(object):
    pass


s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)
# Michael


def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age


from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) # 测试结果
# 25


def set_score(self, score):
    self.score = score

Student.set_score = set_score


s2 = Student() # 创建新的实例

s.set_score(100)
print(s.score)
# 100
s2.set_score(99)
print(s2.score)
# 99

#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称



