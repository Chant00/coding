#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/16/21

@author: Chant
"""


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def heapify(tree, n, i):
    if i >= n:
        return
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    max_node = i
    if c1 < n and tree[c1] > tree[max_node]:
        max_node = c1
    if c2 < n and tree[c2] > tree[max_node]:
        max_node = c2
    if max_node != i:
        swap(tree, max_node, i)
        heapify(tree, n, max_node)


def build_heap(tree, n):
    last_node = n - 1
    parent = int((last_node - 1) / 2)
    for i in range(parent, -1, -1):
        heapify(tree, n, i)


def sort_heap(tree, n):
    build_heap(tree, n)
    for i in range(n - 1, -1, -1):
        swap(tree, i, 0)
        heapify(tree, i, 0)
