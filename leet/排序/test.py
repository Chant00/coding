#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/2/21

@author: Chant
"""
import random
import numpy as np


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


def _partition3(nums, left, right):
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
    print(nums)
    print(f'i={i}, lt:{lt}, gt:{gt}')
    # 想清楚，为什么交换 left 和 lt
    nums[left], nums[lt] = nums[lt], nums[left]
    print(nums)
    return lt, gt


def partition3(arr, low, high):
    """三路快排，将数组分为三个部分, < = >。正常都是分为<= >两部分。可用于解决荷兰旗问题"""
    p1, p2 = low, high
    i = 0
    base = arr[low]
    print(base)
    while i <= p2 and p1 < p2:
        while i <= p2 and arr[i] > base:
            print(f'i={i}, p1:{p1}, p2:{p2}')
            print(arr)
            arr[i], arr[p2] = arr[p2], arr[i]
            p2 -= 1

        if arr[i] < base:
            print(f'i={i}, p1:{p1}, p2:{p2}')
            print(arr)
            arr[i], arr[p1] = arr[p1], arr[i]
            p1 += 1
        i += 1

    print(f'i={i}, p1:{p1}, p2:{p2}')
    print(arr)
    return p1, p2 + 1


def quick_sort(arr, low, high):
    """快速排序"""
    if low < high:  # 这个判断一定要写，否则就会无限递归，超出递归深度，这是递归的终止条件
        p1, p2 = partition3(arr, low, high)
        quick_sort(arr, low, p1 - 1)
        quick_sort(arr, p2, high)
    return arr


a = [90, 3, 6, 2, 8, 90, 11, 87, 91, 94]
_partition3(list(a), 0, len(a) - 1)
a = [3, 6, 2, 8, 11, 87, 90, 90, 94, 91]
p1, p2 = partition3(a, 0, 5)
partition3(a, p2, len(a) - 1)

quick_sort(list(a), 0, len(a) - 1)


def test():
    max_value = 100
    a = np.random.randint(0, max_value, size=10)
    quick_sort(list(a), 0, len(a) - 1)

    for _ in range(30):
        a = np.random.randint(0, 1000, size=100)
        assert quick_sort(list(a), 0, len(a) - 1) == sorted(list(a))

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
