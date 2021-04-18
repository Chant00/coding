# 给一非空的单词列表，返回前 k 个出现次数最多的单词。 
# 
#  返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。 
# 
#  示例 1： 
# 
#  
# 输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# 输出: ["i", "love"]
# 解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
#     注意，按字母顺序 "i" 在 "love" 之前。
#  
# 
#  
# 
#  示例 2： 
# 
#  
# 输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k
#  = 4
# 输出: ["the", "is", "sunny", "day"]
# 解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
#     出现次数依次为 4, 3, 2 和 1 次。
#  
# 
#  
# 
#  注意： 
# 
#  
#  假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。 
#  输入的单词均由小写字母组成。 
#  
# 
#  
# 
#  扩展练习： 
# 
#  
#  尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。 
#  
#  Related Topics 堆 字典树 哈希表 
#  👍 236 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
import random
import heapq
from typing import List


class Solution:
    def topKFrequent2(self, words, k):
        """堆排"""
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """快排"""
        count = collections.Counter(words)
        word_cnt = list(count.items())
        topK = self.findTopK(word_cnt, k, 0, len(word_cnt) - 1)
        topK = sorted(topK, key=lambda x: (-x[1], x[0]))
        return [i[0] for i in topK]

    def findTopK(self, num_cnt, k, low, high):
        # 随机初始化pivot
        pivot = random.randint(low, high)
        base, base_key = num_cnt[pivot][1], num_cnt[pivot][0]
        num_cnt[pivot], num_cnt[low] = num_cnt[low], num_cnt[pivot]

        i = low
        for j in range(low + 1, high + 1):
            if num_cnt[j][1] > base or (
                    num_cnt[j][1] == base and num_cnt[j][0] < base_key):
                i += 1
                num_cnt[i], num_cnt[j] = num_cnt[j], num_cnt[i]

        num_cnt[low], num_cnt[i] = num_cnt[i], num_cnt[low]

        if i == k - 1:
            return num_cnt[:k]
        elif i > k - 1:
            return self.findTopK(num_cnt, k, low, i - 1)
        else:
            return self.findTopK(num_cnt, k, i + 1, high)

# leetcode submit region end(Prohibit modification and deletion)
