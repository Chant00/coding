# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为
# 每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。 
# 
#  示例 1: 
# 
#  输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出: 16 
# 解释: 这两个单词为 "abcw", "xtfn"。 
# 
#  示例 2: 
# 
#  输入: ["a","ab","abc","d","cd","bcd","abcd"]
# 输出: 4 
# 解释: 这两个单词为 "ab", "cd"。 
# 
#  示例 3: 
# 
#  输入: ["a","aa","aaa","aaaa"]
# 输出: 0 
# 解释: 不存在这样的两个单词。 
#  Related Topics 位运算 
#  👍 161 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """怎样快速判断两个字母串是否含有重复数字呢？
        可以为每个字母串建立一个长度为 26 的二 进制数字，每个位置表示是否存在该字母，我们称之为"位掩码"。
        如果两个字母串含有重复数字，那它们的二进制表示 的按位与不为 0。
        同时，我们可以建立一个哈希表来存储（位掩码 -> 单词长度），方便查找调用。"""
        max_prod = 0
        mask_map = dict()  # 使用哈希表来存储（位掩码 -> 单词长度）
        for word in words:
            # 位掩码: 可以为每个字母串建立一个长度为 26 的二进制数字, 每个位置表示是否存在该字母。
            # 如果两个字母串含有重复数字，那它们的二进制表示 的按位与不为 0。
            mask = 0
            for c in word:
                mask |= 1 << ord(c) - ord('a')
            mask_map[mask] = max(mask_map.get(mask, 0), len(word))
            # 对比当前单词与之前的所有单词，无重复字符，且长度乘积大于max_prod则更新max_prod
            for h_mask, h_len in mask_map.items():
                if mask & h_mask == 0:
                    max_prod = max(max_prod, len(word) * h_len)
        return max_prod
# leetcode submit region end(Prohibit modification and deletion)
