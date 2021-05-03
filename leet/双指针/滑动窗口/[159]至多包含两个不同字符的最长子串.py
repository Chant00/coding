# 给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。 
# 
#  示例 1: 
# 
#  输入: "eceba"
# 输出: 3
# 解释: t 是 "ece"，长度为3。
#  
# 
#  示例 2: 
# 
#  输入: "ccaabbb"
# 输出: 5
# 解释: t 是 "aabbb"，长度为5。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 112 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        lookup = dict()
        left, right = 0, 0
        counter = 0
        max_len = 0
        while right < len(s):
            lookup[s[right]] = lookup.get(s[right], 0) + 1
            if lookup[s[right]] == 1:
                counter += 1
            right += 1

            while counter > 2:
                if lookup[s[left]] == 1:
                    counter -= 1
                lookup[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len
# leetcode submit region end(Prohibit modification and deletion)
