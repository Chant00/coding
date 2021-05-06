#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/2/21

@author: Chant
"""
import random
import numpy as np


def _partition3(arr, low, high):
    """三路快排，将数组分为三个部分, < = >。正常都是分为<= >两部分。可用于解决荷兰旗问题
    todo: 这个写法有问题，待修正
    """
    p1, p2 = low, high
    i = low
    base = arr[low]
    while i <= p2:
        while i <= p2 and arr[i] > base:
            arr[i], arr[p2] = arr[p2], arr[i]
            p2 -= 1
        if arr[i] < base:
            arr[i], arr[p1] = arr[p1], arr[i]
            p1 += 1
        i += 1
    return p1, p2 + 1


def partition3(nums, left, right):
    p = nums[left]
    lt = left  # nums[left+1...lt] < base
    gt = right + 1  # nums[gt...right] > base
    # i 这个变量用于遍历数组中的标定点以后的元素
    i = left + 1  # nums[lt+1...i] == base
    # 注意循环可以继续的条件，为什么不可以取“=”
    while i < gt:
        if nums[i] < p:
            lt += 1
            nums[i], nums[lt] = nums[lt], nums[i]
            i += 1
        elif nums[i] == p:
            i += 1
        else:
            gt -= 1
            nums[i], nums[gt] = nums[gt], nums[i]
    # 想清楚，为什么交换 left 和 lt
    nums[left], nums[lt] = nums[lt], nums[left]
    return lt, gt


def quick_sort3(arr, low, high):
    """快速排序"""
    if low < high:  # 这个判断和最后的return一定要写，否则就会无限递归，超出递归深度，这是递归的终止条件
        p1, p2 = _partition3(arr, low, high)
        quick_sort3(arr, low, p1 - 1)
        quick_sort3(arr, p2, high)
    return arr


def test():
    max_value = 100
    a = np.random.randint(0, max_value, size=10)
    quick_sort3(list(a), 0, len(a) - 1)

    for _ in range(30):
        a = np.random.randint(0, 1000, size=100)
        assert quick_sort3(list(a), 0, len(a) - 1) == sorted(list(a))

    """
    b = list(a)
    %timeit merge_sort(b[0:])
    %timeit select_sort(b[0:])
    %timeit insertion_sort(b[0:])
    %timeit shell_sort(b[0:])
    %timeit quick_sort2(b[0:])
    %timeit quick_sort(deepcopy(a), 0, len(a) - 1)
    %timeit quick_sort1(deepcopy(a), 0, len(a) - 1)
    """
