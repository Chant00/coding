#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/2/21

@author: Chant
"""
import random
import numpy as np


def sift_down(arr, start, end):
    parent, child = start, 2 * start + 1
    while child <= end:
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[child] > arr[parent]:
            arr[child], arr[parent] = arr[parent], arr[child]
            parent = child
            child = 2 * parent + 1
        else:
            break
    return arr


def heap_sort(arr):
    for i in range((len(arr) - 2) // 2, -1, -1):
        sift_down(arr, i, len(arr) - 1)

    for j in range(len(arr) - 1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        sift_down(arr, 0, j - 1)
    return arr


def test():
    max_value = 100
    a = np.random.randint(0, max_value, size=10)
    heap_sort(list(a))

    for _ in range(30):
        a = np.random.randint(0, 1000, size=100)
        assert heap_sort(list(a)) == sorted(list(a))

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
