#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/1/21

@author: Chant
"""


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


def merge(left, right):
    l, r = 0, 0
    res = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res.extend(left[l:])
    res.extend(right[r:])
    return res


def merge_sort(arr):
    """归并排序O(nlog(n))"""
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


# 快速排序，随机在数组中选择一个数，遍历分成2个组，比其大的放在右边，比其小的放左边，迭代下去
# 终止条件:left < right，只有一个数时
def quick_sort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quick_sort(arr, left, p - 1)
        quick_sort(arr, p + 1, right)
    return arr


# def partition(arr,left,right):
#         # 设置基准数
#         base = arr[right]
#         i = left
#         for j in range(left,right):
#             # 两个指针，j一直向前，当遍历到比基数大的数时，i,j错位，i停下记下大数的位置，当遇到比j小数时，交换位置；i可以继续向前
#             if arr[j] <= base:
#                 arr[j],arr[i] = arr[i],arr[j]
#                 i += 1
#             print(arr)
#         # 遍历结束后i的位置比基数大，交换
#         arr[i],arr[right] = arr[right],arr[i]
#         return i
def partition(arr, left, right):
    # 设置基准数
    base = arr[left]
    i = left
    for j in range(left + 1, right + 1):
        # 记i为平分点，当遍历到比base大的数后，不变化索引j继续走，比base小时，（将其和i后面一位交换，i前进一位）
        if arr[j] < base:
            arr[j], arr[i + 1] = arr[i + 1], arr[j]
            i += 1
        print(arr)
    # 遍历结束后i的位置比基数大，交换
    arr[i], arr[left] = arr[left], arr[i]
    return i


def quick_sort1(arr, left, right):
    if left >= right:
        return
    low = left
    high = right
    base = arr[low]
    while left < right:
        # 和下面的顺序不能变，从右数将第一个小于基数的赋给
        while arr[right] > base and left < right:
            right -= 1
        arr[left] = arr[right]
        while arr[left] <= base and left < right:
            left += 1
        arr[right] = arr[left]
    arr[left] = base
    quick_sort1(arr, low, left - 1)
    quick_sort1(arr, left + 1, high)
    return arr


quick_sort1([6, 4, 5, 6, 7, 8], 0, 5)


def quick_sort2(arr):
    """超级精简版快速排序 lt:less than  ge:great和equal"""
    if len(arr) <= 1: return arr
    return quick_sort2([lt for lt in arr[1:] if lt < arr[0]]) + arr[0:1] \
           + quick_sort2([ge for ge in arr[1:] if ge >= arr[0]])


def quick_sort():
    pass


def test():
    import numpy as np

    a = np.random.randint(0, 1000, size=10)
    assert all(np.sort(a[1:]) == bubble_sort(a[1:]))
    assert all(np.sort(a[1:]) == select_sort(a[1:]))
    assert all(np.sort(a[1:]) == insertion_sort(a[1:]))
    assert all(np.sort(a[1:]) == shell_sort(a[1:]))
    assert all(np.sort(a[0:]) == merge_sort(a[0:]))
    b = list(a)
    """
    %timeit merge_sort(b[0:])
    %timeit select_sort(b[0:])
    %timeit insertion_sort(b[0:])
    %timeit shell_sort(b[0:])
    %timeit quick_sort2(b[0:])
    """
