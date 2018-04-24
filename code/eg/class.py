#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
import sys

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

def print_score(std):
    print('%s: %s' %(std['name'], std['score']))


class Student(object):
    def __init__(self,name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Bart Simpolere', 2323)
lisa = Student('Lisa', 100)
bart.print_score()
lisa.print_score()



















