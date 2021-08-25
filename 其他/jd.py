#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 8/25/21

@author: Chant
"""


def find_max_sell(arr):
    """
    京东APP拥有百亿级商品。已知某日京东所有销售商品中，有一件商品荣登销量王，其销量占比超过总销量的一半，请找出这个商品。
    假设商品销售日志每条记录一件商品，如【iPhone12，iPhone12，macbookpro16，iPhone12，红米K40】。

    1，2，1，2，1   （1，0）（2，0）（1，0）（2，0）（1，0）
    1，1，1，2，4   （1，0）（1，1）（1，2）（1，1）（1，0）
    """
    counter = [arr[0], 0]
    for i in arr[1:]:
        prev = counter[0]
        if i == prev:
            counter[1] += 1
        else:
            if counter[1] > 0:
                counter[1] -= 1
            else:
                counter[1] = 0
                counter[0] = i
    return counter[0]


def online_distribute(log, login_dict, logout_dict):
    """
    京东APP的活跃用户有4个亿，每个用户从登陆到退出会在一个日志文件中记下登陆时间和退出时间，要求写一个算法，统计一天中京东APP的用户在线分布，粒度为秒。
    [
        (uid, login_time, logout_time),
        (uid, login_time, logout_time),
        (uid, login_time, logout_time),
    ]
    """
    login_dic, logout_dic, = dict(), dict()
    for uid, login_time, logout_time in log:
        login_dic[login_time] = login_dic.get(login_time, 0) + 1
        logout_dic[logout_time] = logout_dic.get(logout_time, 0) + 1
    ans = []
    prev = 0
    for i in range(24 * 60 * 60):
        prev += login_dict[i] - logout_dict[i]
    ans.append(prev)
    return ans


def find_max_sub(nums):
    """
    1、给定一个正整数List，找到序列的最大和。序列中的相邻两个元素不能在原正整数数组中是相邻的。

    输入: [2, 7, 9, 3, 1]
    输出: 12

    2、找到和最大的序列
    输入: [2, 7, 9, 3, 1]
    输出: [2, 9, 1]
    [2, 7, 9, 3, 1]
    2, 7, 11, 11, 12
    """
    n = len(nums)
    dp = [0] * n
    for i in range(n):
        if i == 0:
            dp[i] = nums[0]
        if i == 1:
            dp[i] = max(dp[i - 1], nums[i])
        else:
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    ans = []
    for i in range(2, n):
        if dp[i] != dp[i - 1]:
            ans.append(nums[i])
        if i == 2:
            if dp[i] != dp[i - 1]:
                ans.append(nums[0])
            else:
                ans.append(nums[1])
    return ans
