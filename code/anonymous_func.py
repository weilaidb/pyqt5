#!/usr/bin/python3
# -*- coding: utf-8 -*-

print( list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])) )

def f(x):
    return x * x
f = lambda x: x * x
print(f)
print(f(4))


def build(x, y):
    return lambda: x * x + y * y

print(build)
print(build(3,4))
print(type(build(3,4)))
print(build(3,4))

g = lambda x,y: x * x + y * y

print(g(3,4))
print(type(g))