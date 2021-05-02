# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  k 的取值范围是 [1, 数组中不相同的元素的个数] 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的 
#  
# 
#  
# 
#  进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。 
#  Related Topics 堆 哈希表 
#  👍 728 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import heapq
import collections
import random
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """堆排序"""
        counter = collections.Counter(nums)
        heap = []
        i = 0
        for key, val in counter.items():
            if i < k:
                heapq.heappush(heap, (val, key))
            else:
                if val > heap[0][0]:
                    heapq.heapreplace(heap, (val, key))
            i += 1
        return [i[1] for i in heap]

    def findTopK(self, num_cnt, k, low, high):
        pivot = random.randint(low, high)
        num_cnt[low], num_cnt[pivot] = num_cnt[pivot], num_cnt[low]
        base = num_cnt[low][1]
        i = low

        for j in range(low + 1, high + 1):
            if num_cnt[j][1] > base:
                num_cnt[i + 1], num_cnt[j] = num_cnt[j], num_cnt[i + 1]
                i += 1
        num_cnt[low], num_cnt[i] = num_cnt[i], num_cnt[low]

        if i == k - 1:
            return num_cnt[:k]
        elif i > k - 1:
            return self.findTopK(num_cnt, k, low, i - 1)
        else:
            return self.findTopK(num_cnt, k, i + 1, high)

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        """快排"""
        counter = collections.Counter(nums)
        num_cnt = list(counter.items())
        top_K = self.findTopK(num_cnt, k, 0, len(num_cnt) - 1)
        return [i[0] for i in top_K]

# leetcode submit region end(Prohibit modification and deletion)
