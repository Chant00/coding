#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/2/21

@author: Chant
"""
import random


def counting_sort(arr, max_value):
    bucket_size = max_value + 1
    bucket = [0] * bucket_size
    for i in arr:
        bucket[i] += 1
    idx = 0
    for i in range(bucket_size):
        for _ in range(bucket[i]):
            arr[idx] = i
            idx += 1
    return arr


def sift_down(arr, start, end):
    parent, child = start, 2 * start + 1
    while child < end:
        if child + 1 < end and arr[child] < arr[child + 1]:
            child += 1
        if arr[parent] < arr[child]:
            arr[parent], arr[child] = arr[child], arr[parent]
            parent = child
            child = 2 * parent + 1
        else:
            break
    return arr


def heap_sort(arr):
    # 创建大顶堆
    for start in range((len(arr) - 2) // 2, -1, -1):
        sift_down(arr, start, len(arr))
    # 堆排序
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end)
    return arr


def test():
    import numpy as np
    from copy import deepcopy

    max_value = 100
    a = np.random.randint(0, max_value, size=20)

    counting_sort(list(a), max_value)
    heap_sort(list(a))
    np.sort(a[0:])

    for _ in range(30):
        max_value = 1000
        a = np.random.randint(0, max_value, size=1000)
        # a = sorted(a, reverse=True)
        # a = sorted(a)
        # assert all(np.sort(a[1:]) == bubble_sort(a[1:]))
        # assert all(np.sort(a[1:]) == select_sort(a[1:]))
        # assert all(np.sort(a[1:]) == insertion_sort(a[1:]))
        # assert all(np.sort(a[1:]) == shell_sort(a[1:]))
        # assert all(np.sort(a[0:]) == merge_sort(a[0:]))
        assert all(np.sort(a[0:]) == heap_sort(a[0:]))
        assert all(np.sort(a[0:]) == counting_sort(a[0:], max_value))
        # assert all(quick_sort1(deepcopy(a), 0, len(a) - 1) == np.sort(deepcopy(a)))
        # assert all(quick_sort(deepcopy(a), 0, len(a) - 1) == np.sort(deepcopy(a)))
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
