#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021-07-27

@author: Chant
"""
import numpy as np
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def loss(h, y):
    return -(y * np.log(h) + (1 - y) * np.log(1 - h)).mean()


def gradient(X, h, y):
    """损失函数对w求偏导"""
    return np.dot(X.T, (h - y)) / y.shape[0]


def LR(X, y, lr=0.05, count=10):
    intercept = np.ones((X.shape[0], 1))  # 初始化截距为1
    X = np.concatenate((intercept, X), axis=1)
    w = np.zeros(X.shape[1])  # 初始化参数为0
    # 梯度下降迭代
    for i in range(count):
        z = np.dot(X, w)
        h = sigmoid(z)

        g = gradient(X, h, y)  # 计算梯度
        w -= lr * g  # 通过学习率lr 计算步长并梯度下降

        l = loss(h, y)
        print(l)

    return l, w


def sk_lr():
    """
    调用sklearn LR，训练模型，打印准确率
    :return:
    """
    data = datasets.load_iris()
    X = data['data'][50:150]
    y = data['target'][50:150]
    lr = LogisticRegression()
    lr.fit(X, y)
    print('sklear-lr:', lr.score(X[0:100], y[0:100]))

    l, w = LR(X, y)
