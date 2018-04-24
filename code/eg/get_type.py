#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
import sys
import types


print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type(123) == type(456))
print(type(123) == (int))
print(type('abc') == str)
print(type('abc') ==  type(123))

def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs)== types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

#dir 打印所有ABC的方法
print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())


class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

print('ABC'.lower())





class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
# 紧接着，可以测试该对象的属性：

print('-' * 30)
print(hasattr(obj, 'x'))  # 有属性'x'吗？
# True
# obj.x
# 9
print(hasattr(obj, 'y'))  # 有属性'y'吗？
# False
setattr(obj, 'y', 19)  # 设置一个属性'y'
print(hasattr(obj, 'y'))  # 有属性'y'吗？
# True
print(getattr(obj, 'y'))  # 获取属性'y'
# 19
print(obj.y)  # 获取属性'y'
# 19

# print( getattr(obj, 'z'))
print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

print(dir(obj))
print( hasattr(obj, 'power')) # 有属性'power'吗？
# True
print(getattr(obj, 'power')) # 获取属性'power'
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print(fn) # fn指向obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
print( fn()) # 调用fn()与调用obj.power()是一样的
# 81


def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

