#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 8/5/21

@author: Chant
正负数都有的数组，求其中n-1个元素，乘积最大值
"""


def max_multiply(nums):
    """[-1,3,4,-3,4]"""
    _max = float('-inf')
    n = len(nums)
    for i in range(n):
        _ji = 1
        for j in range(n):
            if j != i:
                _ji *= nums[j]
        _max = max(_ji, _max)
    return _max


print(max_multiply([3, 4, 1, 0, 4]))
