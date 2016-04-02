#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals



def f(x):
    return x*x


def binary_search(f,seq,target):
    low = 0
    high = len(seq)-1

    while high >= low:
        mid = low + (high - low) // 2
        print(low,high,mid)
        if f(seq[mid]) < target: ##higher area
            low = mid + 1
        elif f(seq[mid]) > target:##lower area
            high = mid - 1
        else:
            print('exactly')
            return seq[mid]
    else:
        print('nearly')
        return seq[mid]

import numpy as np
seq = np.arange(0,10,0.000001)
#seq = list('abcdefg')
res = binary_search(f,seq,2)
print(res)

def f(d):
    x = d[0]
    y = d[1]
    head = x + y
    return head

def g(d):
    x = d[0]
    y = d[1]

    foot = 2*x + 4*y
    return foot

from itertools import product

seq = list(product(range(35),range(35)))


def iter_search(f,seq,target):
    for item in seq:
        if f(item) == target:
            yield item

res = list(product(range(35),range(35)))
res = iter_search(f,res,35)
res = iter_search(g,res,94)
print(list(res))


#if __name__ == '__main__':
