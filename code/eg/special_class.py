#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
import sys
import types


class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Michael'))
# <__main__.Student object at 0x109afb190>




class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name

print(Student('Michael'))
# Student object (name: Michael)

s = Student('Michael')
print(s)


class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

aaaa = Student('Michael')
aaaa





class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 1000000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    # def __getitem__(self, n):
    #     a, b = 1, 1
    #     for x in range(n):
    #         a, b = b, a + b
    #     return a

    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print(n)


print('-' * 50)
f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[4])
print(f[5])
print(f[6])
print(f[7])
print(f[8])
print(f[9])
print(f[10])
print(f[11])
print(f[110])

print(list(range(100))[5:10])


f = Fib()
print(f[0:5])
# [1, 1, 2, 3, 5]
print(f[:10])
print(f[:10:2])
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]



class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__





print(Chain().status.user.timeline.list)




class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
s() # self参数不要传入
# My name is Michael.

print('callable-' * 30)
print(callable(Student))
# True
print(callable(max))
# True
print(callable([1, 2, 3]))
# False
print(callable(None))
# False
print(callable('str'))
# False
