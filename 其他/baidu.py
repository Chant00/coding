#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9/14/21

@author: Chant

链表交叉
N(0) N(s-1)
N(0)-> N(s/2-1) -> N(s/2)
N(0)-> N(s/2)

二分查找
[4,5,6,7,0,1,2]
0 4
3 -1
"""


def find(nums, target):
    l, r = 0, len(nums)
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > target > nums[l] or not (nums[mid] < target < nums[r]):
            r = mid - 1
        else:
            l = mid

    return l if l else -1


print(find([4, 5, 6, 7, 0, 1, 2], 3))
print(find([4, 5, 6, 7, 0, 1, 2], 4))
