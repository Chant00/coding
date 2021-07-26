#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 6/8/21

@author: Chant
https://leetcode-cn.com/circle/discuss/Se3QTg/
已知 a,b两个整数组成的数组，每次能够把 a或者 b 里面的数 +1 或者 -1，问最少需要多少次能够使 a 的最大值小于等于 b 的最小值?
例: a=[1,2,3], b=[2,7,8];
答: 1 次，把 a 中的 3 减—，最大值为 2，小于等于 b 的最小值。
"""
from bisect import *


def solve(A, B):
    """O(nlgn+mlgm+32lg(mn)); n=len(A); m=len(B)"""
    A.sort()
    B.sort()
    nA = len(A)
    l, r = B[0], A[-1]  # l是B最小值, r是A最大值
    if l >= r: return 0
    # 为使得修改次数最小, 修改A,B元素后, A最大值必然等于B最小值, 假设为k
    # k的取值范围是[l,r]左闭右闭
    # A,B修改次数一共为f(k)=sum(k-e for e in B if e<k) + sum(e-k for e in A if e>k)
    # 一阶离散导数 Δf = f(k+1)-f(k) = sum(1 for e in B if e<=k) - sum(1 for e in A if e>k)
    # 不难发现Δf是增函数, 那么让Δf第一次>0的k就是题目所求的k之一
    # 以下二分查找第一个让Δf>0的k
    # `nA-bisect_right(A,k)` 就是A中>k的数的数量; `bisect_right(B,k)` 就是B中<=k的数的数量
    while l < r:
        m = l + (r - l) // 2  # 作为加分项, 如果A,B是int32[], 用c++/java写需要特别留意溢出问题
        if bisect_right(B, m) - (nA - bisect_right(A, m)) > 0:
            r = m
        else:
            l = m + 1
    # 这一行, l值存的就是这个k;
    return sum(l - e for e in B if e < l) + sum(e - l for e in A if e > l)


print(solve([1000, 200, 3, 12312, 3, 123, 12, 312, 3, 123], [1, 2, 3, 4, 5, 6, 7, 3, 43, 45, 35, 345, 21]))
# expected 14058
