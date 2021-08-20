#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 8/20/21

@author: Chant
一个01数组，求出现0、1出现次数相等的最长子串的长度
"""


def max_sub(nums):
    """O(n)
    先把0转为-1，用字字典遍历时记录前缀和为key索引为value，相同的前缀和，说明这两个索引之间的数和为0，即之前01数量相等。
    """
    max_len = 0
    _sum = 0
    dic = {0: -1}
    for i, num in enumerate(nums):
        _sum += num if num else -1
        if _sum in dic:
            max_len = max(max_len, i - dic[_sum])
        else:
            dic[_sum] = i
    return max_len


def max_sub1(num):
    """O(n^2)超时"""
    max_len = 0
    for i in range(len(num)):
        _sum = num[i]
        for j in range(i + 1, len(num)):
            _sum = _sum + num[j]
            if _sum * 2 == j - i + 1 and _sum * 2 > max_len:
                max_len = _sum * 2
    return max_len


max_sub([1, 0, 0, 1, 0])
max_sub([1, 0, 0, 1, 0, 1])
