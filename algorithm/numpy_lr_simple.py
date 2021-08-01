#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021-07-27

@author: Chant
"""
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def loss(h, y):
    return -(y * np.log(h) + (1 - y) * np.log(1 - h)).mean()


def gradient(X, h, y):
    """损失函数对w求偏导
    h'(x)=h(x)(1-h(x))  h(x)代表sigmoid函数
    h = h(wx) h代表预测值

    loss = -y*log(h(wx)) - (1-y)log(1-h(wx))
    loss'(w) = -y*h'(w)/h(wx) - (1-y)*(-h'(w))/(1-h(wx))
             = -y*(h(1-h)*x)/h - (1-y)*(-h(1-h)*x)/(1-h)
             = x[-y(1-h) + (1-y)h]
             = x(h-y)
    """
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


class MyLR:
    def __init__(self, lr=0.05, max_ite=10):
        self.lr = lr
        self.max_ite = max_ite
        self.w = None

    def predict(self, X, threshold=0.6):
        intercept = np.ones((X.shape[0], 1))
        X = np.concatenate((intercept, X), axis=1)
        h = sigmoid(np.dot(X, self.w))
        if threshold is None:
            return h
        return np.array([1 if i > threshold else 0 for i in h])

    def fit(self, X, y):
        # 补上截距项
        intercept = np.ones((X.shape[0], 1))
        X = np.concatenate((intercept, X), axis=1)

        self.w = np.zeros(X.shape[1])  # 初始化参数为0

        for i in range(self.max_ite):
            h = sigmoid(np.dot(X, self.w))
            g = gradient(X, h, y)
            self.w -= self.lr * g
            print(f'epoch = {i}, loss = {loss(h, y)}')

    def score(self, X, y):
        from sklearn.metrics import accuracy_score
        return accuracy_score(y, self.predict(X))


def sk_lr():
    """
    调用sklearn LR，训练模型，打印准确率
    :return:
    """
    data = datasets.load_iris()
    X = data['data'][50:150]
    y = data['target'][50:150]
    # 由于y里面是1和2，所以清洗一下标签
    y = np.array([i - 1 for i in y])
    lr = LogisticRegression()
    lr.fit(X, y)
    print('sklear-lr:', lr.score(X[0:100], y[0:100]))

    # l, w = LR(X, y)
    my_lr = MyLR(max_ite=300)
    my_lr.fit(X, y)
    my_lr.predict(X)
    print('numpy-lr:', my_lr.score(X, y))


sk_lr()
