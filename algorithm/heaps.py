#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/16/21

@author: Chant
"""
import heapq
import random


class MaxHeap:
    def __init__(self):
        self.data = []
        self.count = 0

    def add(self, item):
        """往最大堆中添加元素：
        1. 首先把新添加的元素当做最后一个叶子节点添加到堆的最后面
        2. 判断当前节点和其父节点的大小：若当前节点大于父节点，那么交换两个节点的位置；然后继续往上比较，直到当前节点小于其父节点（即在_shiftUp函数中实现的逻辑）
        """
        self.data.append(item)
        self.sift_up(self.count)
        self.count += 1

    def sift_up(self, index):
        parent = (index - 1) >> 1
        while index > 0 and self.data[parent] < self.data[index]:
            self.data[parent], self.data[index] = self.data[index], self.data[parent]
            index = parent
            parent = (index - 1) >> 1

    def pop(self):
        """从最大堆中弹出根节点，该元素肯定是这个堆中最大的元素；调整堆的结构使得新的堆仍是一个最大堆：
        1. 首先弹出根节点（也就是索引为0的元素），然后把最后一个叶子节点放到根节点位置
        2. 从根节点开始，比较其与两个子节点的大小：当当前节点小于其子节点时，则将当前节点与较大的一个子节点交换位置，然后继续往下比较，直到当前节点是叶子节点或者当前节点大于子节点
        """
        ret = self.data[0]
        self.data[0] = self.data[self.count - 1]
        self.count -= 1
        self.sift_down(0)
        return ret

    def sift_down(self, index):
        max_child = (index << 1) + 1
        while max_child < self.count:
            # 判断最大子节点
            if max_child + 1 < self.count and self.data[max_child] < self.data[max_child + 1]:
                max_child = max_child + 1
            if self.data[index] >= self.data[max_child]:
                break
            self.data[index], self.data[max_child] = self.data[max_child], self.data[index]
            index = max_child
            max_child = (index << 1) + 1


# 元素是数值类型
def testIntValue():
    for iTimes in range(10):
        iLen = random.randint(1, 300)
        allData = random.sample(range(iLen * 100), iLen)
        #         allData = [1, 4, 3, 2, 5, 7, 6]
        #         iLen = len(allData)
        print('\nlen =', iLen)

        oMaxHeap = MaxHeap()
        print('_data:\t   ', allData)
        arrDataSorted = sorted(allData, reverse=True)
        print('dataSorted:', arrDataSorted)
        for i in allData:
            oMaxHeap.add(i)
        heapData = []
        for i in range(iLen):
            iExpected = arrDataSorted[i]
            iActual = oMaxHeap.pop()
            heapData.append(iActual)
            print('{0}, expected: {1}, actual: {2}'.format(iExpected == iActual, iExpected, iActual))
            assert iExpected == iActual, ""
        print('dataSorted:', arrDataSorted)
        print('heapData:  ', heapData)


# 元素是元祖类型
def testTupleValue():
    for iTimes in range(10):
        iLen = random.randint(1, 300)
        listData = random.sample(range(iLen * 100), iLen)
        #         listData = [1, 4, 3, 2, 5, 7, 6]
        #         iLen = len(listData)
        # 注意：key作为比较大小的关键
        allData = dict(zip(listData, [str(e) for e in listData]))
        print('\nlen =', iLen)
        print('allData: ', allData)

        oMaxHeap = MaxHeap()
        arrDataSorted = sorted(allData.items(), key=lambda d: d[0], reverse=True)
        #         arrDataSorted = sorted(allData, reverse=True)
        print('dataSorted:', arrDataSorted)
        for (k, v) in allData.items():
            oMaxHeap.add((k, v))  # 元祖的第一个元素作为比较点
        heapData = []
        for i in range(iLen):
            iExpected = arrDataSorted[i]
            iActual = oMaxHeap.pop()
            heapData.append(iActual)
            print('{0}, expected: {1}, actual: {2}'.format(iExpected == iActual, iExpected, iActual))
            assert iExpected == iActual, ""
        print('dataSorted:', arrDataSorted)
        print('heapData:  ', heapData)


# 元素是自定义类
def testClassValue():
    class Model4Test(object):
        '''
        用于放入到堆的自定义类。注意要重写__lt__、__ge__、__le__和__cmp__函数。
        '''

        def __init__(self, sUid, value):
            self._sUid = sUid
            self._value = value

        def getUid(self):
            return self._sUid

        def getValue(self):
            return self._value

        # 类类型，使用的是小于号_lt_
        def __lt__(self, other):  # operator <
            #             print('in __lt__(self, other)')
            return self.getValue() < other.getValue()

        def __ge__(self, other):  # oprator >=
            return self.getValue() >= other.getValue()

        # 下面两个方法重写一个就可以了
        def __le__(self, other):  # oprator <=
            return self.getValue() <= other.getValue()

        def __cmp__(self, other):
            # call global(builtin) function cmp for int
            return super.cmp(self.getValue(), other.getValue())

        def __str__(self):
            return '({0}, {1})'.format(self._value, self._sUid)

    for iTimes in range(10):
        iLen = random.randint(1, 300)
        listData = random.sample(range(iLen * 100), iLen)
        #         listData = [1, 4, 3, 2, 5, 7, 6]
        allData = [Model4Test(str(value), value) for value in listData]
        print('allData:   ', [str(e) for e in allData])
        iLen = len(allData)
        print('\nlen =', iLen)

        oMaxHeap = MaxHeap()
        arrDataSorted = sorted(allData, reverse=True)
        print('dataSorted:', [str(e) for e in arrDataSorted])
        for i in allData:
            oMaxHeap.add(i)
        heapData = []
        for i in range(iLen):
            iExpected = arrDataSorted[i]
            iActual = oMaxHeap.pop()
            heapData.append(iActual)
            print('{0}, expected: {1}, actual: {2}'.format(iExpected == iActual, iExpected, iActual))
            assert iExpected == iActual, ""
        print('dataSorted:', [str(e) for e in arrDataSorted])
        print('heapData:  ', [str(e) for e in heapData])


if __name__ == '__main__':
    testIntValue()
    testTupleValue()
    testClassValue()
