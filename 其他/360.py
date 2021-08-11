#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 8/11/21

@author: Chant
输入：
vector<int> 100,150,2000,500
map<int, int> (150,1) (300,4)

输出：
150,100,180,300,2000,500

如果只能额外分配len(map)的空间，线性时间复杂度能完成么
"""


def merge(arr, map):
    size = len(arr) + len(map)
    i, j = 0, 0
    res = []
    reversed_map = {v - 1: k for k, v in map.items()}
    while i < size:
        if i in reversed_map:
            v = reversed_map.pop(i)
            res.append(v)
        else:
            if arr[j] not in map:
                res.append(arr[j])
            j += 1
        i += 1
    if reversed_map:
        res.extend(list(reversed_map.values()))
    return res


merge([100, 180, 2000, 500], dict([(150, 4), (300, 1)]))
