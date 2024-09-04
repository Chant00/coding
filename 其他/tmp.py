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


def cal_auc(labels, preds):
    pairs = sorted(zip(labels, preds), key=lambda x: x[1])
    pairs.append((0, -1))
    m, n = 0, -1
    rank_sum = 0
    window_rank_sum, window_size, window_pos = 0, 0, 0
    prev_rank, prev_label, prev_score = 0, 0, -1

    for rank, (label, score) in enumerate(pairs, start=1):
        if prev_label == 1:
            m += 1
        else:
            n += 1
        if prev_score == score:
            window_rank_sum += prev_rank
            window_size += 1
            if prev_label == 1:
                window_pos += 1
        else:
            if window_size > 0:
                window_rank_sum += prev_rank
                window_size += 1
                if prev_label == 1:
                    window_pos += 1
                rank_sum += window_rank_sum / window_size * window_pos
                window_rank_sum, window_size, window_pos = 0, 0, 0
            else:
                if prev_label == 1:
                    rank_sum += prev_rank
        prev_rank, prev_label, prev_score = rank, label, score
    return (rank_sum - m * (m + 1) / 2) / (m * n)



from sklearn.metrics import roc_curve, auc


def sk_learn_auc(labels, pre):
    fpr, tpr, th = roc_curve(labels, pre, pos_label=1)
    return auc(fpr, tpr)


labels = [0, 1, 1, 0, 0, 1, 1, 1]
preds = [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.8, 0.9]
print(cal_auc(labels, preds))
print(auc2(labels, preds))
print(sk_learn_auc(labels, preds))
print("==============")


def test():
    import numpy as np
    threshold = 1e-5
    for length in np.random.randint(0, 1000, 10):
        labels = np.random.randint(0, 2, length)
        pre = np.round(np.random.random(length), 2)
        print(cal_auc(labels, pre))
        real_auc = sk_learn_auc(labels, pre)
        print(real_auc)
        assert cal_auc(labels, pre) - real_auc < threshold


test()
