# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  示例 4: 
# 
#  
# 输入: s = ""
# 输出: 0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 5 * 104 
#  s 由英文字母、数字、符号和空格组成 
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 5340 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = dict()
        left, right = -1, 0
        max_len = 0
        while right < len(s):
            if s[right] in lookup and lookup[s[right]] > left:
                left = lookup[s[right]]
            else:
                print(f'l:{left},r:{right}')
                max_len = max(max_len, right - left)
            lookup[s[right]] = right
            right += 1
        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i - k)
        return res

    def lengthOfLongestSubstring1(self, s: str) -> int:
        lookup = dict()
        counter = 0
        left, right = 0, 0
        max_len = 0
        while right < len(s):
            lookup[s[right]] = lookup.get(s[right], 0) + 1
            if lookup[s[right]] > 1:
                counter += 1
            right += 1

            while counter > 0:
                if lookup[s[left]] > 1:
                    counter -= 1
                lookup[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len
# leetcode submit region end(Prohibit modification and deletion)
