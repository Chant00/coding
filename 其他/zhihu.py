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
        # 以及这里,l作为右边界，需要l+1
        if l - n + 1 >= 0 and alpha[l - n + 1:l + 1] == beta:
            alpha = alpha[:l - n + 1] + alpha[l + 1:]
            m -= n
        else:
            l += 1

    return alpha


print(remove_sub('ababccabcaaa', 'abc'))
print(remove_sub('abaabcaaabcaaa', 'abc'))

"""
计算完全二叉树的节点数量
叶子节点的高度差不超过一
最后一层最左边连续排列
[1,2,3,4,5]
2*n+1 2*n+2
root
m代表层数
1
2
2**(m-1)
2**m-1=n
m = lg(n-1)

2**(lg(n-1)-1)
n
"""

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def num_of_tree(root):
    cnt = 1
    layer1 = [root]
    layer2 = []
    while True:
        for i in layer1:
            if i.left:
                layer2.append(i.left)
            if i.right:
                layer2.append(i.right)

        cnt += len(layer2)
        if layer2[0].left is None and layer2[0].right is None:
            break
        layer1 = layer2
        layer2 = []

    return cnt
