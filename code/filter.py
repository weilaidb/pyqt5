# -*- coding: utf-8 -*-
import os
import sys


def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1,2,3,4,5,6,7,8,9,10])))
print(type(list(filter(is_odd, [1,2,3,4,5,6,7,8,9,10]))))



def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


def _odd_iter():
    n = 1
    while True:
        n = n + 1
        # print("n is ", n )
        yield  n


def _not_divisible(n):
    return lambda x: x % n > 0



def primes():
    yield 2
    it = _odd_iter()
    print("type it is:", type(it))
    # print(list(it)) #Memory Error ,over flow
    while True:
        n = next(it)
        print("get n is:", n )
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 10:
        print(n)
    else:
        break





def test_yield():
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6


for n in range(10):
    print((test_yield()))

