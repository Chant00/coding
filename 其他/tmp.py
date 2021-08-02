#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021-08-02

@author: Chant
二叉树的之字形层序遍历
限定语言：Kotlin、Typescript、Python、C++、Groovy、Rust、Java、Go、Scala、Javascript、Ruby、Swift、Php、Python 3
给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）
例如：
给定的二叉树是{3,9,20,#,#,15,7},
"""


class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        res = []
        res.append([root.val])
        layer1 = [root]
        layer2 = []
        cnt = 1
        while layer1:
            for i in layer1:
                if i.left is not None:
                    layer2.append(i.left)
                if i.right is not None:
                    layer2.append(i.right)

            if layer2:
                if cnt % 2 == 0:
                    res.append([i.val for i in reversed(layer2)])
                else:
                    res.append([i.val for i in layer2])
            layer1 = layer2
            layer2 = []
            cnt += 1
        return res

        # write code here
