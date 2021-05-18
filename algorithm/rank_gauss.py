#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/13/21

@author: Chant
"""
import numpy as np
from scipy.special import erfinv
import matplotlib.pyplot as plt


def scale_minmax(x):
    '''归一化'''
    return (x - x.min()) / (x.max() - x.min())


def scale_norm(x):
    '''标准化'''
    return (x - x.mean()) / x.std()


def scale_rankgauss(x, epsilon=1e-6):
    '''rankgauss'''
    x = x.argsort().argsort()  # rank
    x = (x / x.max() - 0.5) * 2  # scale
    x = np.clip(x, -1 + epsilon, 1 - epsilon)
    x = erfinv(x)
    return x


x = np.random.randint(0, 100, 1000)
plt.hist(x)
plt.show()

x_norm = scale_norm(x)
x_minmax = scale_minmax(x)
x_rankgauss = scale_rankgauss(x)

plt.hist(x_norm, bins=50)
plt.show()

plt.hist(x_minmax, bins=50)
plt.show()

plt.hist(x_rankgauss, bins=50)
plt.show()
