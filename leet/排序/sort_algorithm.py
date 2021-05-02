#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/1/21

@author: Chant
"""
import random
import numpy as np


def bubble_sort(arr):
    """O(n^2)外圈循环每次将最大值放到最右边"""
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def select_sort(arr):
    """O(n^2)类似冒泡，不过内层循环只记录最小值的索引，外层循环，交换一次将最小值放到最左边"""
    for i in range(len(arr) - 1):
        min_idx = i  # 记录最小数的索引
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # i 不是最小数时，将 i 和最小数进行交换
        if min_idx != i:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr


def insertion_sort(arr):
    """O(n^2)对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。"""
    for i in range(1, len(arr)):
        cur = arr[i]
        pre_idx = i - 1
        while pre_idx >= 0 and arr[pre_idx] > cur:
            arr[pre_idx + 1] = arr[pre_idx]
            pre_idx -= 1
        arr[pre_idx + 1] = cur
    return arr


def shell_sort(arr):
    """希尔排序，O(n^(3/2)), 最坏O(n^2)"""
    n = len(arr)
    gap = n // 2  # 初始步长
    while gap > 0:
        for i in range(gap, n):  # 每个步长进行插入排序
            tmp = arr[i]
            j = i - gap  # pre_idx
            while j >= 0 and arr[j] > tmp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = tmp
        gap = gap // 2  # 得到新的步长
    return arr


def getSedgewickStepArr(n):
    """Sedgewick增量序列 最坏时间复杂度为𝑂(𝑁^(4/3))；平均时间复杂度约为𝑂(𝑁^(7/6))
    D=9*4^i-9*2^i+1 或 4^(i+2)-3*2^(i+2)+1 , i>=0
    稍微变一下形：D=9*(2^(2i)-2^i)+1 或 2^(2i+4)-3*2^(i+2)+1 , i>=0
    """
    i = 0
    arr = []
    while True:
        tmp = 9 * ((1 << 2 * i) - (1 << i)) + 1
        if tmp <= n:
            arr.append(tmp)
        tmp = (1 << 2 * i + 4) - 3 * (1 << i + 2) + 1
        if tmp <= n:
            arr.append(tmp)
        else:
            break
        i += 1
    return arr


def shellSort(arr):
    """希尔排序（Sedgewick增量序列）"""
    n = len(arr)
    # 获取Sedgewick增量序列
    stepArr = getSedgewickStepArr(n)
    for step in reversed(stepArr):
        for i in range(step, n):
            j = i
            tmp = arr[j]
            while j >= step:
                if tmp < arr[j - step]:
                    arr[j] = arr[j - step]
                    j -= step
                else:
                    break
            arr[j] = tmp
    return arr

def merge_sort():
    pass


def quick_sort():
    pass


a = np.random.randint(0, 1000, size=10)
assert all(np.sort(a[1:]) == bubble_sort(a[1:]))
assert all(np.sort(a[1:]) == select_sort(a[1:]))
assert all(np.sort(a[1:]) == insertion_sort(a[1:]))
assert all(np.sort(a[1:]) == shell_sort(a[1:]))
