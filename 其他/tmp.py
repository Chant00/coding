#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021-08-02

@author: Chant
二叉树的之字形层序遍历
限定语言：Kotlin、Typescript、Python、C++、Groovy、Rust、Java、Go、Scala、Javascript、Ruby、Swift、Php、Python 3
给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）
例如：
给定的二叉树是{3,9,20,#,#,15,7},
"""


def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # arr[i], arr[high] = arr[high], arr[i]
    return i - 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr


def _partition3(arr, low, high):
    """三路快排，将数组分为三个部分, < = >。正常都是分为<= >两部分。可用于解决荷兰旗问题"""
    p1, p2 = low, high
    i = low  # 注意这里，总是写错成i=0！！！所有的这种都是经常将边界写成0或者len(arr)-1, 但是这里是low和high是会在递归中变化的
    base = arr[low]
    while i <= p2:
        while i <= p2 and arr[i] > base:  # 注意这里要用while而非if，因为此时可能arr[p2]> base，所以交换后依旧arr[i] > base，需要让p2前进继续交换
            arr[i], arr[p2] = arr[p2], arr[i]
            p2 -= 1
        if arr[i] < base:
            arr[i], arr[p1] = arr[p1], arr[i]
            p1 += 1
        i += 1
    return p1, p2 + 1


def quick_sort3(arr, low, high):
    """快速排序"""
    if low < high:  # 这个判断和最后的return一定要写，否则就会无限递归，超出递归深度，这是递归的终止条件
        p1, p2 = _partition3(arr, low, high)
        quick_sort3(arr, low, p1 - 1)
        quick_sort3(arr, p2, high)
    return arr


def test():
    # import numpy as np
    # import random
    #
    # a = np.random.randint(0, 1000, size=10)
    # quick_sort(list(a), 0, len(a) - 1)
    # a = [974, 353, 20, 439, 15, 154, 435, 630, 178, 219]
    # partition(a, 0, len(a) - 1)
    # a = [219, 353, 20, 439, 15, 154, 435, 630, 178, 974]
    a = [1, 2, 1, 0, 0, 0, 0, 1, 2, 2, 2, 1, 1, 1]
    _partition3(a, 0, len(a) - 1)
    # quick_sort3(a, 0, len(a) - 1)


test()
