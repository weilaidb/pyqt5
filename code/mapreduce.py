# -*- coding: utf-8 -*-
import os
import sys

#所有的字符串首字母大小，其余小写


def normalize(name):
    return name.capitalize()

L1 = ['admin', 'GOOD', 'TEST']
L2 = list(map(normalize,L1))
print(L2)

