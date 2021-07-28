#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021-07-27

@author: Chant
https://blog.csdn.net/ABCDABCD321123/article/details/104732240/
"""

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据集
data = pd.read_csv('/Users/chant/PycharmProjects/coding/algorithm/data/credit-a.csv', header=None)
data.head()
data.iloc[:, -1].value_counts()

# 构造x,y
x = data.iloc[:, :-1]
y = data.iloc[:, -1].replace(-1, 0)
# 构建一个 输入为 15 隐藏层为 10 10 输出层为1的神经网络，由于是逻辑回归，最后输出层的激活函数为sigmoid
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, input_shape=(15,), activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.summary()

# 设置优化器、损失函数
model.compile(
    optimizer='adam',  # 优化器
    loss='binary_crossentropy',  # 损失函数，交叉熵
    metrics=['acc']  # 准确率
)
# 训练80次
history = model.fit(x, y, epochs=80)
