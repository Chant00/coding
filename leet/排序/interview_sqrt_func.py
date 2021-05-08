#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
求平方根
Created on 2018/5/4

@author: Chant
"""
import math
from math import sqrt


def sqrt_bi(n):
    """为了方便起见，先假设n为正数"""
    low = 0  # 设置下限为0
    # max(num, 1)因为小于1的时候，平方根是大于原值的。e.g: 0.2 ** 2 = 0.04但0.2 > 0.04
    high = max(n, 1)  # 设置上限为n和1之中的最大数，即：如果n>=1，那么上限为n；如果n<1，那么上限为1
    guess = (low + high) / 2  # 先从中间值开始猜
    count = 1  # 设置猜测次数起始值为1
    while abs(
            guess ** 2 - n) > 0.00000000000000000001 and count < 100:  # 当猜测值的平方和n本身的差值无限接近误差值时，循环才会停止；同时设置猜测次数不超过100次
        if guess ** 2 < n:  # 如果猜测值的平方小于n，那么将此设为下限
            low = guess
        else:  # 如果猜测值的平方大于n，那么将此设为上限
            high = guess
        guess = (low + high) / 2  # 根据新的上下限，重新进行猜测
        count += 1  # 猜测次数每次增加1
    return guess


def binary_sqrt(num, threshold=0.0001, iterations=100):
    """
    二分法:为了方便起见，先假设n为正数

    过程示例：求根号5
    a:折半：       5/2=2.5
    b:平方校验:  2.5*2.5=6.25>5，并且得到当前上限2.5
    c:再次向下折半:2.5/2=1.25
    d:平方校验：1.25*1.25=1.5625<5,得到当前下限1.25
    e:再次折半:2.5-(2.5-1.25)/2=1.875
    f:平方校验：1.875*1.875=3.515625<5,得到当前下限1.875
    :return:
    """
    low = 0  # 设置下限为0
    # max(num, 1)因为小于1的时候，平方根是大于原值的。e.g: 0.2 ** 2 = 0.04但0.2 > 0.04
    high = max(num, 1)  # 设置上限为n和1之中的最大数，即：如果n>=1，那么上限为n；如果n<1，那么上限为1
    guess = num / 2  # 先从中间值开始猜
    count = 0  # 设置猜测次数起始值为1,记录迭代次数
    # 当猜测值的平方和n本身的差值无限接近误差值时，循环才会停止；同时设置猜测次数不超过100次
    while abs(guess ** 2 - num) > threshold and count < iterations:
        if guess ** 2 < num:  # 如果猜测值的平方小于n，那么将此设为下限
            low = guess
        else:  # 如果猜测值的平方大于n，那么将此设为上限
            high = guess
        guess = (high + low) / 2  # 根据新的上下限，重新进行猜测
        count += 1  # 猜测次数每次增加1
    print(count)
    return guess


def sgd_sqrt(n, learning_rate=0.001, threshold=0.0001):
    """梯度下降法
    损失函数Loss: f(x, n) = (x**2 - n)**2
    求导：df/dx = 2*(x**2-n) * 2*x
    :return:
    """
    x = n
    count = 0
    while x ** 2 - n > threshold:
        x_gradient = learning_rate * 2 * (x ** 2 - n) * 2 * x
        x -= x_gradient
        # print(x)
        count += 1
    print('迭代次数：', count)
    return x


def sgd_sqrt2(n, learning_rate=0.001, threshold=0.0001):
    """梯度下降法
    损失函数Loss: f(x, n) = x**3 / 3 - n*x
    求导：df/dx = x**2-n
    :return:
    """
    x = n
    count = 0
    while x ** 2 - n > threshold:
        x_gradient = learning_rate * (x ** 2 - n)
        x -= x_gradient
        # print(x)
        count += 1
    print('迭代次数：', count)
    return x


def newton_sqrt(n, threshold=0.0001):
    """牛顿法求平方根 https://www.zhihu.com/question/20690553
    泰勒展开式
    收敛的充分条件：若f二阶可导，那么在待求的零点x周围存在一个区域，只要起始点x0位于这个邻近区域内，那么牛顿-拉弗森方法必定收敛。
    损失函数：f(x,n) = x**2 - n
    Xn点切线的方程 todo: 怎么求的？g(X0)=f(X0),g'(X0)=f'(X0).就是一阶泰勒展开式
        用一阶泰勒展开得：f(Xn)+f'(Xn)(X-Xn) 令其等于0解得下一个点X(n+1) = Xn - f(Xn)/f'(Xn)
    迭代：x' = x - f(x)/f'(x) = (x + n/x)/2
    :param n:
    :param threshold:
    :return:
    """
    x = n
    count = 0
    while abs(x ** 2 - n) > threshold:
        x = (x + n / x) / 2
        # print(x)
        count += 1
    print('迭代次数：', count)
    return x


def newton_sqrt2(n, threshold=0.0001):
    """使用二阶泰勒展开式g(x)，即：用二次曲线逼近，求此二次曲线g(x)的最小值，也就是g'(x)=0的解
    原理来自：https://wenku.baidu.com/view/c09a2510f18583d0496459aa.html
    牛顿法求平方根 https://www.zhihu.com/question/20690553
    泰勒展开式
    收敛的充分条件：若f二阶可导，那么在待求的零点x周围存在一个区域，只要起始点x0位于这个邻近区域内，那么牛顿-拉弗森方法必定收敛。
    损失函数：f(x,n) = x**2 - n
    Xn点切线的方程 todo: 怎么求的？g(X0)=f(X0),g'(X0)=f'(X0).就是一阶泰勒展开式
        用一阶泰勒展开得：f(Xn)+f'(Xn)(X-Xn) 令其等于0解得下一个点X(n+1) = Xn - f(Xn)/f'(Xn)
    迭代：x' = x - f(x)/f'(x) = (x + n/x)/2
    :param n:
    :param threshold:
    :return:
    """
    x = n
    count = 0
    while abs(x ** 2 - n) > threshold:
        x = 2 * x ** 3 / (3 * x ** 2 - n)
        # print(x)
        count += 1
    print(count)
    return x


def test(func):
    for n in list(range(3, 6)) + [0.1, 0.6, 0.7]:
        print(func(n))
        assert func(n) == sqrt(n), "wrong sqrt function"


def main():
    test(sqrt_bi)
    test(binary_sqrt)


def even_first(arr):
    """在不使用额外空间的前提下， 将数组中的偶数放在奇数前面
    思路：
        使用两个指针，
        i：奇数指针，i从前往后走，遇到奇数停下，
        j：偶数指针；j从后往前走，遇到偶数停下，
        每次交换两者的数据，当两者相遇，则退出循环。
    """
    # assert arr, 'got an empty list!'
    # arr为空就直接返回空，但是这里不需要像下面这样检查，
    # 因为空数组的话，i小于j，直接就调过循环了
    # if not arr:
    #     return
    i = 0
    j = len(arr) - 1
    while i < j:
        # while arr[i] % 2 == 0:
        while arr[i] < 3:
            i += 1
        # while arr[i] % 2 != 0:
        while arr[j] >= 3:
            j -= 1
        # 注意这里的限制条件，在最后一次循环的时候，也会出现i>=j的情况，而这时不能交换
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]


def even_first_test():
    for a in [[], [1], [1, 3, 5, 7, 9, 8, 6, 4, 2],
              [2, 4, 6, 8, 9, 7, 5, 3, 1], [1, 2, 3, 5, 4, 6, 7, 3, 5, 6]]:
        even_first(a)
        print(a)


def even_first2(arr):
    """
    i与j都从前面开始
    arr在0到i（不包括i）之间为奇数
    arr在i到j之间都为偶数
    """
    assert arr, 'got an empty list!'
    i = 0
    j = 0
    while j < len(arr):
        # & 1 与 % 2 结果相同。&是位运算符，计算更快，不过懒得背，就用%2吧
        if arr[j] & 1:
            if j != i:
                arr[j], arr[i] = arr[i], arr[j]
            i += 1
        j += 1
    return arr


def even_first3(arr):
    return sorted(arr, key=lambda x: x % 2)


# ======================
def find_greatest_sub_array(arr):
    """连续子数组的最大和
    题目：输入一个整形数组，数组里有正数也有负数，数组中的一个或连续多个整数组成一个子数组。
    求所有子数组的和的最大值。要求时间复杂度为O(n)。

    sum_of_array记录当前子组和，当子组合<0,则重置为0，重新开始计和
    greatest_sum记录目前出现过最大的子组和
    """
    assert arr, 'Inappropriate argument, got an empty list!'

    sum_of_array = 0
    greatest_sum = arr[0]

    for number in arr:
        sum_of_array += number

        if sum_of_array > greatest_sum:
            greatest_sum = sum_of_array

        if sum_of_array < 0:
            sum_of_array = 0

    return greatest_sum


def find_greatest_sub_array_test():
    arrays = [[7, 4, 5, 6, 7, 8, 2, 7, 9], [-21, -4, -6, -9, -2, -3],
              [-4, 12, -8, 9, -9, -2], []]
    for array in arrays:
        print(find_greatest_sub_array(array))


if __name__ == '__main__':
    # print(sqrt_bi(5))
    # print(binary_sqrt(5))
    # print(sgd_sqrt(5))
    # print('*-' * 50)
    # print(newton_sqrt(5))
    # print('*-' * 50)
    # print(newton_sqrt_2(5))
    even_first_test()
    # find_greatest_sub_array_test()
