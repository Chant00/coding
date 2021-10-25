#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 8/25/21

@author: Chant
参考: https://blog.csdn.net/jeryjeryjery/article/details/80245924
"""
import random


class NegativeSampler:
    def __init__(self, table_size=-1, power=0.75):
        self.word_freq = {'a': 20, 'b': 11, 'c': 70}
        self.vocab = list(self.word_freq.items())
        self.vocab_size = len(self.vocab)
        #
        self.power = power
        if table_size == -1:
            self.table_size = sum(self.word_freq.values())
            print(f'INFO: table_size is auto set to {self.table_size}')
        else:
            self.table_size = table_size
        #
        self.table = {}
        self.init_unigram_table()

    def init_unigram_table(self):
        # 计算分母，total_pow表示总的词的概率，不是直接用每个词的频率，而是频率的0.75次方幂
        total_pow = 0
        for i in self.word_freq.values():
            total_pow += pow(i, self.power)
        # 计算分子，每个词在table中占的小格子数是不一样的，频率高的词，占的格子数显然多
        i = 0
        d1 = pow(self.vocab[i][1], self.power) / total_pow
        for j in range(self.table_size):
            self.table[j] = self.vocab[i][0]
            if j / self.table_size > d1:  # j与d1都等比例缩放到0-1之间
                i += 1
                d1 += pow(self.vocab[i][1], self.power) / total_pow
            # 有很小的概率出现超出vocab的部分，直接给到最后一个词
            if i >= self.vocab_size:
                print(f'INFO: i exceed vocab_size, i={i}, vocab_size={self.vocab_size}')
                i = self.vocab_size - 1

    def sample(self):
        return self.table[random.randrange(0, self.table_size)]

    def stat_check(self, n_test=1000):
        stat = dict()
        for _ in range(n_test):
            word = self.sample()
            stat[word] = stat.get(word, 0) + 1
        print('stat:', sorted(stat.items(), key=lambda x: x[1]))
        print('word_freq', sorted(self.word_freq.items(), key=lambda x: x[1]))


def test():
    ns = NegativeSampler(power=1, table_size=-1)
    ns.stat_check()
    ns = NegativeSampler(power=0.75, table_size=-1)
    ns.stat_check()
    ns = NegativeSampler(power=0.4, table_size=-1)
    ns.stat_check()

    ns.sample()
