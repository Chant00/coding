#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 8/25/21

@author: Chant
实测，基于bisect的bisect_bin2idx最快，
基本数字落在第二个分箱之后，bisect_bin2idx 就比bin2idx快了，前两个分箱，差距也只有10几ns。

参照word2vec中Negative Sample的打点表方法实现的dst.fast_bin2idx，
由于int((v - self._min) / self.length * self.table_size) 这部分数学计算较耗时，
只有在分箱长度大于2720时，才能优于bisect_bin2idx，且还有精度问题

n_bins = 10
print(bin2idx(bins, val))
4
%timeit bisect_bin2idx(bins, val)  # 这里最快
192 ns ± 2.53 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
%timeit dst.fast_bin2idx(val)
406 ns ± 13.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
%timeit bin2idx(bins, val)
353 ns ± 5.44 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
%timeit dst.math_test(val)
273 ns ± 3.26 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

n_bins = 20
print(bin2idx(bins, val))
13
%timeit bisect_bin2idx(bins, val) # 这里最快
208 ns ± 4.4 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
%timeit dst.fast_bin2idx(val)
393 ns ± 5.13 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
%timeit bin2idx(bins, val)
768 ns ± 6.77 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
%timeit dst.math_test(val)
263 ns ± 6.99 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

n_bins =2720
print(bin2idx(bins, val))
1325
%timeit bisect_bin2idx(bins, val)
409 ns ± 5.52 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
%timeit dst.fast_bin2idx(val) # 这里最快
404 ns ± 8.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
%timeit bin2idx(bins, val) # 这里单位直接跃升到微秒了
74.6 µs ± 1.65 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
%timeit dst.math_test(val)
259 ns ± 5.9 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

n_bins =5000
print(bin2idx(bins, val))
3462

%timeit bisect_bin2idx(bins, val)
426 ns ± 5.57 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
%timeit dst.fast_bin2idx(val) # 这里最快
395 ns ± 6.46 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
%timeit bin2idx(bins, val) # 这里单位直接跃升到微秒了
194 µs ± 4.01 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
%timeit dst.math_test(val)
262 ns ± 7.63 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)


"""
from bisect import bisect_left
from collections import Counter

import numpy as np
from sklearn.preprocessing import KBinsDiscretizer


class Discretizer:
    def __init__(self):
        self.boundary = load_dict()
        for name, bins in self.boundary.items():
            # 去除左边界，因为bisect_left
            self.boundary[name] = bins[1:]
            if len(bins) > 2720:
                print(f'INFO: name={name},len(bins)={len(bins)} exceed 2720, '
                      f'suggest to use LargeDiscretizer().fast_bin2idx()')

    def bin2idx(self, name, v):
        return bisect_left(self.boundary[name], v)


class Discretizer2:
    def __init__(self, table_sizes=dict()):
        self.boundary = load_dict()
        self.parameter_dic = dict()
        for name, bins in self.boundary.items():
            if name in table_sizes:
                table_size = table_sizes[name]
            else:
                table_size = 10000
                print(f'INFO: table_size of {name} auto set to {table_size}')
            self.parameter_dic[name] = LargeDiscretizer(bins, table_size)

    def bin2idx(self, name, v):
        return self.parameter_dic[name].fast_bin2idx(v)


def get_bound_discrete(data, n_bins, strategy):
    f_data = np.array(data).reshape((-1, 1))
    return KBinsDiscretizer(n_bins, encode='ordinal', strategy=strategy).fit(f_data).bin_edges_


def load_dict():
    return {
        'a': list(range(10, 20, 1)),
        'b': sorted(np.random.randint(1, 100, size=10)),
        'c': sorted(np.random.random(size=10)),
        'd': sorted(np.random.randn(10)),
    }


def bin2idx(bins, val):
    """bins不包含最小最大值"""
    index = 0
    for border in bins:
        if val > border:
            index += 1
        else:
            return index
    # 超出了bins中的最大值
    return index


def bisect_bin2idx(bins, val):
    """bins不包含最小最大值"""
    return bisect_left(bins, val)


class LargeDiscretizer:
    def __init__(self, bins, table_size):
        self.bins = bins
        self.inner_bins = bins[1:-1]
        self.table, self.table_size, self._min, self._max, self.length = self.init_table(bins, table_size)

    @staticmethod
    def init_table(bins, table_size=1000, scale=10):
        _min, _max = bins[0], bins[-1]
        length = _max - _min
        # table_size = int(length * scale)
        table = dict()
        i = 1
        d1 = (bins[i] - _min) / length
        for j in range(table_size):
            # print(f' j={j}, i={i}, d1={d1}, j / table_size={j / table_size}')
            table[j] = i - 1
            if j / table_size > d1:
                i += 1
                d1 = (bins[i] - _min) / length
            if i >= len(bins):
                print(f'INFO: i exceed len(bins), i={i}, len(bins)={len(bins)}')
                i -= 1

        if i < len(bins) - 1:
            raise Exception(f'ERROR: i less than len(bins)-1, i={i}, len(bins)={len(bins)}')
        return table, table_size, _min, _max, length

    def fast_bin2idx(self, v):
        if v < self._min:
            return 0
        elif v > self._max:
            return len(self.bins) - 2
        return self.table[int((v - self._min) / self.length * self.table_size)]

    def math_test(self, v):
        return int((v - self._min) / self.length * self.table_size)


def test():
    a = np.random.randn(10000) * 5000
    a = sorted(a)
    get_bound_discrete(a, 500, 'uniform')

    n_bins, strategy = 10, 'uniform'
    data = np.array(a).reshape((-1, 1))
    est = KBinsDiscretizer(n_bins, encode='ordinal', strategy=strategy).fit(data)
    est.transform(data)
    # 去掉最小最大值
    raw_bins = np.round(est.bin_edges_[0], 2).tolist()
    bins = np.round(est.bin_edges_[0], 2).tolist()[1:-1]

    est.transform([[1]])
    dst = LargeDiscretizer(raw_bins, 8000)

    val = 99
    val = 80
    val = 50
    val = 9683
    val = -1100
    val = -14321
    val = -17585.76
    val = 16876
    val = 9075
    print(int(est.transform([[val]])[0][0]))
    print(bin2idx(bins, val))
    print(bisect_bin2idx(bins, val))
    print(dst.fast_bin2idx(val))

    """
    %timeit bisect_bin2idx(bins, val)
    %timeit dst.fast_bin2idx(val)
    
    %timeit bin2idx(bins, val)
    
    %timeit dst.math_test(val)
    """
