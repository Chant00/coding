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
"""
from collections import deque
from typing import List


def func(nums: List[int]) -> List[int]:
    que = [[(0, nums[0])]]
    n = len(nums) - 1
    while que:
        path = que.pop(0)
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
