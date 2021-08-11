#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 8/11/21

@author: Chant
9.编程题
给一个字符串 alpha 和另一个字符串 beta 返回字符串 alpha 去除 beta 后的字串，实例说明 alpha:ababccabcaaa; beta:abc 返回 aaa
alpha:abaabccabcaaa; beta:abc 返回 abacaaa
"""


def remove_sub(alpha, beta):
    m, n = len(alpha), len(beta)
    l = 0
    while l < m and l + n <= m:
        if alpha[l:l + n] == beta:
            alpha = alpha[:l] + alpha[l + n:]
            m -= n
        # 注意这里的两个if的层级
        if l - n + 1 >= 0 and alpha[l - n + 1:l + 1] == beta:
            alpha = alpha[:l - n + 1] + alpha[l + 1:]
            m -= n
        else:
            l += 1

    return alpha


print(remove_sub('ababccabcaaa', 'abc'))
print(remove_sub('abaabcaaabcaaa', 'abc'))
