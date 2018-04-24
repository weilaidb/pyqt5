#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
import sys


print(int('12345'))
print(int('12345', base=8))
print(int('12345', 16))

def int2(x, base=2):
    return int(x, base)

print(int2('010111111111'))



import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))


print(int2('1000000', base=10))

kw = { 'base': 2 }
print(int('10010', **kw))


max2 = functools.partial(max, 10)
max2(5, 6, 7)
print(max2(5, 6, 7))


print(sys.path)