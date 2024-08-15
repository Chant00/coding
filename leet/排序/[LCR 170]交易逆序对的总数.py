# 在股票交易中，如果前一天的股价高于后一天的股价，则可以认为存在一个「交易逆序对」。请设计一个程序，输入一段时间内的股票交易记录 record，返回其中存在的
# 「交易逆序对」总数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入：record = [9, 7, 5, 4, 6]
# 输出：8
# 解释：交易中的逆序对为 (9, 7), (9, 5), (9, 4), (9, 6), (7, 5), (7, 4), (7, 6), (5, 4)。
#  
# 
#  
# 
#  限制： 
# 
#  0 <= record.length <= 50000 
# 
#  Related Topics 树状数组 线段树 数组 二分查找 分治 有序集合 归并排序 👍 1108 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """使用归并排序计算逆序对，使用左闭右开的区间
    初始化tmp，重复利用这个tmp，比切片省内存
    """

    def merge_sort(self, record: List[int], tmp, s, e) -> int:
        # 先定义递归的终止条件
        inverse_count = 0
        # 注意：这里不能用==，针对record=[]的特殊情况，s=e=0, 此时s>e-1
        if s >= e - 1:
            return inverse_count

        mid = s + (e - s) // 2
        inverse_count += self.merge_sort(record, tmp, s, mid)
        inverse_count += self.merge_sort(record, tmp, mid, e)

        l, r, pos = s, mid, s
        while l < mid and r < e:
            # 注意：如果只是排序，<和<=不影响结果，但计算逆序对的时候不同。
            # if record[l] < record[r]:
            if record[l] <= record[r]:
                tmp[pos] = record[l]
                l += 1
                inverse_count += r - mid
            else:
                tmp[pos] = record[r]
                r += 1
            pos += 1

        for i in range(l, mid):
            tmp[pos] = record[i]
            inverse_count += r - mid
            pos += 1
        for i in range(r, e):
            tmp[pos] = record[i]
            pos += 1

        record[s:e] = tmp[s:e]
        return inverse_count

    def reversePairs(self, record: List[int]) -> int:
        n = len(record)
        tmp = [0] * n
        return self.merge_sort(record, tmp, 0, n)


Solution().reversePairs([1, 3, 2, 3, 1])


class Solution2:
    """官方题解，使用左闭右闭的区间"""

    def mergeSort(self, record, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(record, tmp, l, mid) + self.mergeSort(record, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if record[i] <= record[j]:
                tmp[pos] = record[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = record[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = record[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = record[k]
            pos += 1
        record[l:r + 1] = tmp[l:r + 1]
        return inv_count

    def reversePairs(self, record: List[int]) -> int:
        n = len(record)
        tmp = [0] * n
        return self.mergeSort(record, tmp, 0, n - 1)

# leetcode submit region end(Prohibit modification and deletion)
