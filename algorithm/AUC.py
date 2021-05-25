#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/25/21

@author: Chant
"""
from sklearn.metrics import roc_curve, auc


def sk_learn_auc(labels, pre):
    fpr, tpr, th = roc_curve(labels, pre, pos_label=1)
    return auc(fpr, tpr)


def auc1(label, pre):
    """方法一 统计分类器对正样本的打分高于负样本的概率 复杂度：O(M*N)"""
    pos = [i for i in range(len(label)) if label[i] == 1]
    neg = [i for i in range(len(label)) if label[i] == 0]

    auc = 0
    for i in pos:
        for j in neg:
            if pre[i] > pre[j]:
                auc += 1
            elif pre[i] == pre[j]:
                auc += 0.5

    return auc / (len(pos) * len(neg))


def auc2(labels, pre):
    """方法二，排序后按照公式计算，预测值相同时，rank值取平均。
    使用窗口统计预测值相同时的情况，并计算平均值。复杂度：O(M+N)
    需要注意的点：
        1. 窗口需要加上上一个样本，且上一个样本为正样本时其rank值会被多加一次，所以需要减一次
        2. 连续和非连续窗口的情况
    """
    pos, neg, rank_sum = 0, 0, 0
    pairs = sorted(zip(labels, pre), key=lambda x: x[1])
    pairs.append((0, -1))  # 添加哑变量，多加了一个负样本，后面neg-=1，目的是多迭代一次，最后一次窗口计算一下，否则就需要赋值粘贴代码手动多迭代一次
    prev_score, prev_label, prev_rank = -1, 0, 0  # prev_score预设为-1，rank==1时，就能自动跳过窗口操作
    window_rank_sum, window_size, window_pos = 0, 0, 0  # 评分相同的样本，进入窗口，之后计算平均rank
    for rank, (label, score) in enumerate(pairs, start=1):
        if label == 1:
            pos += 1
        else:
            neg += 1

        if score == prev_score:
            window_rank_sum += rank
            window_size += 1
            if label == 1:
                window_pos += 1
        else:
            if window_size > 0:
                # 窗口中需要添加prev样本
                if prev_label == 1:
                    rank_sum -= prev_rank  # rank_sum中移除prev_rank，后面会在窗口中加上取平均后的rank
                    window_pos += 1
                window_rank_sum += prev_rank
                window_size += 1
                rank_sum += window_pos * window_rank_sum / window_size
                # 清空窗口
                window_rank_sum, window_size, window_pos = 0, 0, 0
            # 只要score != prev_score就加一次rank，以应对连续窗口的情况
            if label == 1:
                rank_sum += rank
            prev_score, prev_label, prev_rank = score, label, rank

    return (rank_sum - pos * (1 + pos) / 2) / (pos * (neg - 1))


def getAuc(labels, pre):
    """方法2的另一种写法
    将pred数组的索引值按照pred[i]的大小正序排序，返回的sorted_pred是一个新的数组，
    sorted_pred[0]就是pred[i]中值最小的i的值，对于这个例子，sorted_pred[0]=8
    """
    sorted_pred = sorted(range(len(pre)), key=lambda i: pre[i])
    pos = 0.0  # 正样本个数
    neg = 0.0  # 负样本个数
    auc = 0.0
    last_pre = pre[sorted_pred[0]]
    count = 0.0
    pre_sum = 0.0  # 当前位置之前的预测值相等的rank之和，rank是从1开始的，所以在下面的代码中就是i+1
    pos_count = 0.0  # 记录预测值相等的样本中标签是正的样本的个数
    for i in range(len(sorted_pred)):
        if labels[sorted_pred[i]] > 0:
            pos += 1
        else:
            neg += 1

        if last_pre != pre[sorted_pred[i]]:  # 当前的预测概率值与前一个值不相同
            # 对于预测值相等的样本rank需要取平均值，并且对rank求和
            auc += pos_count * pre_sum / count
            count = 1
            pre_sum = i + 1  # 更新为当前的rank
            last_pre = pre[sorted_pred[i]]
            if labels[sorted_pred[i]] > 0:
                pos_count = 1  # 如果当前样本是正样本 ，则置为1
            else:
                pos_count = 0  # 反之置为0
        else:
            pre_sum += i + 1  # 记录rank的和
            count += 1  # 记录rank和对应的样本数，pre_sum / count就是平均值了
            if labels[sorted_pred[i]] > 0:  # 如果是正样本
                pos_count += 1  # 正样本数加1
    auc += pos_count * pre_sum / count  # 加上最后一个预测值相同的样本组
    auc -= pos * (pos + 1) / 2  # 减去正样本在正样本之前的情况
    auc = auc / (pos * neg)  # 除以总的组合数
    return auc


def test():
    labels = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    pre = [0.9, 0.8, 0.3, 0.1, 0.4, 0.9, 0.66, 0.7, 0.7, 0.7, 0.8, 0.8, 0.81]
    print(auc1(labels, pre))
    print(getAuc(labels, pre))
    print(auc2(labels, pre))

    fpr, tpr, th = roc_curve(labels, pre, pos_label=1)
    print(auc(fpr, tpr))

    import numpy as np
    length = 100
    threshold = 1e-5
    for length in np.random.randint(0, 1000, 10):
        labels = np.random.randint(0, 2, length)
        pre = np.random.random(length)
        real_auc = sk_learn_auc(labels, pre)
        assert auc1(labels, pre) - real_auc < threshold
        assert auc2(labels, pre) - real_auc < threshold
        assert getAuc(labels, pre) - real_auc < threshold
