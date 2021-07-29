#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 7/29/21

@author: Chant
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""


def check(arr, start, end):
    parent, child = start, 2 * start + 1
    while child <= end:
        if child + 1 <= end and arr[child + 1] < parent:
            return False
        if arr[child] > arr[parent]:
            return False
    return True


def check_bst(arr):
    for i in range((len(arr) - 2) // 2, -1, -1):
        is_bst = check(arr, i, len(arr))
        if not is_bst:
            return False
    return True
