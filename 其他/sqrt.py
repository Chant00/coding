#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 8/25/21

@author: Chant
"""


def subtriplicate(num, threshold):
    """立方根,二分法"""
    l, r = (0, num) if num >= 1 else (num, 1)
    while l < r:
        mid = (l + r) / 2
        if abs(mid ** 3 - num) <= threshold:
            break
        if num < mid ** 3:
            r = mid
        else:
            l = mid
    return mid


print(subtriplicate(0.9 ** 3, 0.001))
print(subtriplicate(9 ** 3, 0.001))
print(subtriplicate(1 ** 3, 0.001))
