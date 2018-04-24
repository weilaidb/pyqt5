#!/usr/bin/python3
# -*- coding: utf-8 -*-

def now():
    print('2015-3-25')


f = now
f()

print(now.__name__)
print(f.__name__)



def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')

print('-' * 33)
now()


# now = log('execute')(now)
# now()



import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator



import time, functools

def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, time.time()))
    return fn

# 测试
@metric
def fast(x, y):
    time.sleep(1.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

print('-' * 33)
f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print("测试成功")
print("game over")