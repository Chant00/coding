#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9/6/21

@author: Chant
跳棋和LCS最长公共子序列

跳棋问题：
[1,2,3,1,4,5,6,7,3]
从下标为0的地方出发，每次可以向左或向右走一步，或者直接跳到相同数字处，比如从下标为0的1直接跳到下标为3的1
示例中的最短路径是3， 即1->1->3->3


这个题解法应该是，预先吧每个位置上的{"左”,"右","跳"}位置整理好，然后从第一个位置开始广搜，第一个达到末尾的就是最短的那个路径


排列组合的题
输入n, 输出所有n个括号的和合法序列。
比如()(())是合法的，)(())是非法的。

我的解法，回溯法+栈判断是否合法
"""
from collections import deque
from typing import List


def func(nums: List[int]) -> List[int]:
    """保存路径"""
    que = deque([[(0, nums[0])]])
    # que = [[(0, nums[0])]]
    n = len(nums) - 1
    while que:
        # path = que.pop(0)
        path = que.popleft()
        i, num = path[-1]
        if i == n:
            return path
        if i > 0:
            que.append(path + [(i - 1, nums[i - 1])])
        if i < n:
            que.append(path + [(i + 1, nums[i + 1])])
        for j in range(n + 1):
            if j != i and nums[j] == num:
                que.append(path + [(j, nums[j])])


print(func([1, 2, 2, 3, 1, 4, 5, 1, 6, 7, 3]))


def minJump(nums: List[int]) -> int:
    """只计算最短步长"""
    que = deque([(0, 0)])
    n = len(nums)
    step = 0
    while que:
        i, step = que.popleft()
        if i == n - 1:
            break
        if i > 0:
            que.append((i - 1, step + 1))
        if i < n - 1:
            que.append((i + 1, step + 1))
        for j in range(n):
            if i != j and nums[i] == nums[j]:
                que.append((j, step + 1))
    return step


print(minJump([1, 2, 3, 1, 4, 5, 6, 7, 3]))
