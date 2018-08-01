#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string

def generateRandomChar():
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 1))
    print (salt)
    return  salt

def generateRandomCharN(n):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, n))
    print (salt)
    return  salt