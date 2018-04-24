#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import numpy
import sys
import types

# from enum import Enum
from enum import Enum, unique


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)



#@unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6



day1 = Weekday.Mon
print(day1)
# Weekday.Mon
print(Weekday.Tue)
# Weekday.Tue
print(Weekday['Tue'])
# Weekday.Tue
print(Weekday.Tue.value)
# 2
print(day1 == Weekday.Mon)
# True
print(day1 == Weekday.Tue)
# False
print(Weekday(1))
# Weekday.Mon
print(day1 == Weekday(1))
# True
# Weekday(7)
# Traceback (most recent call last):
#   ...
# ValueError: 7 is not a valid Weekday
for name, member in Weekday.__members__.items():
     print(name, '=>', member)
# ...
# Sun => Weekday.Sun
# Mon => Weekday.Mon
# Tue => Weekday.Tue
# Wed => Weekday.Wed
# Thu => Weekday.Thu
# Fri => Weekday.Fri
# Sat => Weekday.Sat
