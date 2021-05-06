#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/1/21

@author: Chant

快排，归并排序，每天写一次，知道写对多次
"""
import numpy as np
import random


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


def hoare_partition(arr, low, high):
    """第一版划分算法，由C.R.Hoare设计，见算法导论习题7-1。
    双路快排，等于pivot的元素不做处理，当出现很多等于pivot的元素时，能更大概率地分布在pivot的左右，
    不会将它们全部归到左边，导致算法复杂度退化为O(n^2)。
    这里使用base这个临时变量，实现交换的操作，不过其实在python可以直接交换两个变量的值，直接用原版的方式就可以
    """
    base = arr[low]
    l, r = low, high
    while l < r:
        # 下面两个while的顺序不能变，必须让right先走
        # NOTE1 注意这里和NOTE2里的<=对应,
        # 如果改为NOTE > 和NOTE < 则很可能死循环，如果一个是< 一个是>=则退化为和partition一样了
        while arr[r] >= base and l < r:
            r -= 1
        arr[l] = arr[r]

        while arr[l] <= base and l < r:  # NOTE2
            l += 1
        arr[r] = arr[l]
    arr[l] = base
    return l


def partition(arr, low, high):
    """设置arr[right]为基准数，小于基准的就从往左边放。代码会稍微优雅一点，没有那么多+1。算法导论的原始版本"""
    base = arr[high]
    i = low
    for j in range(low, high):  # 注意，这里容易写错成range(high)
        # 两个指针，j一直向前，当遍历到比基数大的数时，i,j错位，i停下记下大数的位置，当遇到比j小数时，交换位置；i可以继续向前
        if arr[j] <= base:  # < 或<=都行
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    # 遍历结束后i的位置比基数大，交换
    arr[i], arr[high] = arr[high], arr[i]
    return i


def partition2(arr, low, high):
    """设置arr[left]为基准数，小于基准的就从往左边放。LeetCode官方题解中常见。"""
    base = arr[low]
    i = low
    for j in range(low + 1, high + 1):  # 注意，这里容易写错range
        # 记i为平分点，当遍历到比base大的数后，不变化索引j继续走，比base小时，（将其和i后面一位交换，i前进一位）
        if arr[j] < base:  # < 或<=都行
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    # 遍历结束后i的位置比基数大，交换
    arr[i], arr[low] = arr[low], arr[i]
    return i


def randomized_partition(arr, low, high):
    """针对最坏情况（正序或倒序的，划分后刚好分为n-1个和0个元素），随机选择pivot
    但是对于完全是同一个元素的情况，三路快排才是解决之道
    """
    rand = random.randint(low, high)
    arr[rand], arr[low] = arr[low], arr[rand]
    return partition(arr, low, high)


def quick_sort(arr, low, high):
    """快速排序"""
    if low < high:  # 这个判断一定要写，否则就会无限递归，超出递归深度，这是递归的终止条件
        p = randomized_partition(arr, low, high)
        # p = hoare_partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr


def _partition3(arr, low, high):
    """三路快排，将数组分为三个部分, < = >。正常都是分为<= >两部分。可用于解决荷兰旗问题
    todo: 这个写法有问题，待修正
    """
    p1, p2 = low, high
    i = 0
    base = arr[low]
    while i <= p2:
        while i <= p2 and arr[i] > base:
            arr[i], arr[p2] = arr[p2], arr[i]
            p2 -= 1
        if arr[i] < base:
            arr[i], arr[p1] = arr[p1], arr[i]
            p1 += 1
        i += 1
    return p1, p2


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
    # 想清楚，为什么交换 left 和 lt, 以为nums[left]是base，需要放到中间那部分里
    nums[left], nums[lt] = nums[lt], nums[left]
    return lt, gt


def quick_sort3(arr, low, high):
    """快速排序"""
    if low < high:  # 这个判断和最后的return一定要写，否则就会无限递归，超出递归深度，这是递归的终止条件
        p1, p2 = partition3(arr, low, high)
        quick_sort(arr, low, p1 - 1)
        quick_sort(arr, p2, high)
    return arr


def quick_sort2(arr):
    """超级精简版快速排序，空间占用大"""
    if len(arr) <= 1: return arr
    return quick_sort2([lt for lt in arr[1:] if lt < arr[0]]) + arr[:1] + \
           quick_sort2([ge for ge in arr[1:] if ge >= arr[0]])


def sift_down(arr, start, end):
    """从根节点开始，比较其与两个子节点的大小：当当前节点小于其子节点时，则将当前节点与较大的一个子节点交换位置，
    然后继续往下比较，直到当前节点是叶子节点或者当前节点大于子节点"""
    parent, child = start, 2 * start + 1  # 初始化根节点和最大子节点，暂时将左子节点视为最大子节点
    while child <= end:  # 这里的end是左闭右闭的，也可以写成左闭右开，外面传end进来时就不用-1，以及后面改为child + 1 < end
        # 左子节点和右子节点比较，更新最大子节点
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        # 根节点小于最大子节点，交换节点值，并将root指针移动到子节点上，将child指针移动到新root的子节点上
        if arr[parent] < arr[child]:
            arr[parent], arr[child] = arr[child], arr[parent]
            # root, child = child, 2 * root + 1 # 千万不能这么写，这么写child还是原来的child，并没有更新
            parent = child  # 更新根节点和子节点
            child = 2 * parent + 1
        else:
            break
    return arr


def heap_sort(arr):
    """堆排序，重复从大顶堆取出数值最大的结点(把根结点和最后一个结点交换，把交换后的最后一个结点移出堆)，
    并让残余的堆维持最大堆积性质。"""
    # 创建大顶堆 # len(arr) - 2) // 2，因为: last_node = len(arr)-1, parent=(last_node-1)//2
    for start in range((len(arr) - 2) // 2, -1, -1):
        sift_down(arr, start, len(arr) - 1)

    # 堆排序
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)
    return arr


def heapify(tree, n, i):
    if i >= n:
        return
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    max_node = i
    if c1 < n and tree[c1] > tree[max_node]:
        max_node = c1
    if c2 < n and tree[c2] > tree[max_node]:
        max_node = c2
    if max_node != i:
        tree[max_node], tree[i] = tree[i], tree[max_node]
        heapify(tree, n, max_node)


def heap_sort2(arr):
    """递归的方式实现堆排序"""
    # len(arr) - 2) // 2，因为: last_node = len(arr)-1, parent=(last_node-1)//2
    for start in range((len(arr) - 2) // 2, -1, -1):
        heapify(arr, len(arr), start)
    for end in range((len(arr) - 1), 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0)
    return arr


def counting_sort(arr, max_value):
    """计数排序"""
    # 初始化桶，对于arr中的数字i，bucket[i]等于数字i在arr中的出现次数
    bucket_len = max_value + 1
    bucket = [0] * bucket_len
    for i in arr:
        bucket[i] += 1
    # 填值回arr
    idx = 0
    for j in range(bucket_len):
        for _ in range(bucket[j]):
            arr[idx] = j
            idx += 1
    return arr


def test():
    a = np.random.randint(0, 1000, size=10)
    quick_sort(list(a), 0, len(a) - 1)
    partition3(a, 0, len(a) - 1)

    for _ in range(30):
        a = np.random.randint(0, 1000, size=100)
        assert quick_sort(list(a), 0, len(a) - 1) == sorted(list(a))
        assert quick_sort3(list(a), 0, len(a) - 1) == sorted(list(a))

        assert bubble_sort(list(a)) == sorted(list(a))
        assert select_sort(list(a)) == sorted(list(a))
        assert insertion_sort(list(a)) == sorted(list(a))

        assert shell_sort(list(a)) == sorted(list(a))

        assert merge_sort(list(a)) == sorted(list(a))
        assert heap_sort(list(a)) == sorted(list(a))
        assert quick_sort(list(a), 0, len(a) - 1) == sorted(list(a))

        assert counting_sort(list(a), max_value=1000) == sorted(list(a))
    """
    b = list(a)
    %timeit select_sort(list(a))
    %timeit insertion_sort(list(a))
    %timeit shell_sort(list(a))
    %timeit merge_sort(list(a))
    %timeit quick_sort(list(a), 0, len(a) - 1)
    %timeit quick_sort1(list(a), 0, len(a) - 1)
    %timeit quick_sort2(list(a))
    %timeit sorted(list(a))
    
    %timeit merge_sort(list(a))
    %timeit quick_sort(list(a), 0, len(a) - 1)
    %timeit counting_sort(list(a), 1000)
    %timeit heap_sort(list(a))
    %timeit heap_sort2(list(a))
    """
