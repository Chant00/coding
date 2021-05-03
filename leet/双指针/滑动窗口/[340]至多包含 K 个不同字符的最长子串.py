# 给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。 
# 
#  示例 1: 
# 
#  输入: s = "eceba", k = 2
# 输出: 3
# 解释: 则 T 为 "ece"，所以长度为 3。 
# 
#  示例 2: 
# 
#  输入: s = "aa", k = 1
# 输出: 2
# 解释: 则 T 为 "aa"，所以长度为 2。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 122 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        lookup = dict()
        left, right = 0, 0
        counter = 0
        max_len = 0
        while right < len(s):
            lookup[s[right]] = lookup.get(s[right], 0) + 1
            if lookup[s[right]] == 1:
                counter += 1
            right += 1
            while counter > k:
                if lookup[s[left]] == 1:
                    counter -= 1
                lookup[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len
# leetcode submit region end(Prohibit modification and deletion)
