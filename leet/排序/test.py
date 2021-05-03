#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/2/21

@author: Chant
"""
import random


def quick_sort1(arr, low, high):
    """常见的双指针双向奔赴快排"""
    if low >= high:
        return arr
    # 随机选取基准数
    rand = random.randint(low, high)
    arr[rand], arr[low] = arr[low], arr[rand]
    base = arr[low]
    l, r = low, high
    while l < r:
        # 下面两个while的顺序不能变，必须让right先走
        while arr[r] > base and l < r:
            r -= 1
        arr[l] = arr[r]

        while arr[l] <= base and l < r:  # 注意<=因为上面是arr[r] > base
            l += 1
        arr[r] = arr[l]
    arr[l] = base
    quick_sort1(arr, low, l - 1)
    quick_sort1(arr, l + 1, high)
    return arr


def partition(arr, low, high):
    rand = random.randint(low, high)
    arr[rand], arr[high] = arr[high], arr[rand]
    i = low
    for j in range(low, high):
        if arr[j] < arr[high]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_sort(arr, low, high):
    if low >= high:
        return arr
    i = partition(arr, low, high)
    quick_sort(arr, low, i - 1)
    quick_sort(arr, i + 1, high)
    return arr


def test():
    import numpy as np
    from copy import deepcopy

    a = np.random.randint(0, 1000, size=10)

    quick_sort(deepcopy(a), 0, len(a) - 1)
    quick_sort1(deepcopy(a), 0, len(a) - 1)

    for _ in range(30):
        a = np.random.randint(0, 1000, size=1000)
        a = sorted(a, reverse=True)
        a = sorted(a)
        # assert all(np.sort(a[1:]) == bubble_sort(a[1:]))
        # assert all(np.sort(a[1:]) == select_sort(a[1:]))
        # assert all(np.sort(a[1:]) == insertion_sort(a[1:]))
        # assert all(np.sort(a[1:]) == shell_sort(a[1:]))
        # assert all(np.sort(a[0:]) == merge_sort(a[0:]))
        # assert all(quick_sort1(deepcopy(a), 0, len(a) - 1) == np.sort(deepcopy(a)))
        assert all(quick_sort(deepcopy(a), 0, len(a) - 1) == np.sort(deepcopy(a)))
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
