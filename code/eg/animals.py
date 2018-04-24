#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
import sys


class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass



dog = Dog()
dog.run()

cat = Cat()
cat.run()


