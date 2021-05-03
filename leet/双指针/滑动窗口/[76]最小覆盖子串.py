# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
# 
#  注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 105 
#  s 和 t 由英文字母组成 
#  
# 
#  
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？ Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 1118 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """重点是要理解，lookup中1是临界点"""
        lookup = dict()
        for ch in t:
            lookup[ch] = lookup.get(ch, 0) + 1
        # Q1: counter = len(lookup)，那么后面的判断是lookup[s[r]] == 0，如果是len(t)那么后面的判就得改为lookup[s[r]] >= 0
        count = len(lookup)

        l = r = 0
        start, min_len = 0, len(s) + 1

        while r < len(s):
            if s[r] in lookup:
                lookup[s[r]] -= 1
                # 这里的判断重点是要理解lookup中的值代表什么，1是一个临界点
                if lookup[s[r]] == 0:  # 因为先操作了lookup[s[r]] -= 1，否则就是lookup[s[r]] == 1
                    count -= 1
            r += 1

            while count == 0:
                if s[l] in lookup:
                    lookup[s[l]] += 1
                    if lookup[s[l]] == 1:
                        count += 1
                        # Q2: 为什么min_len的更新不能放在while循环外？因为求的是最小值，left在移动过程中窗口长度会越来越小，但是这些窗口是不满足条件的。
                        if r - l < min_len:  # 这里总是写错成>
                            start, min_len = l, r - l
                l += 1
        return s[start:start + min_len] if min_len < len(s) + 1 else ''

    def minWindow1(self, s: str, t: str) -> str:
        """重点是要理解，lookup中1是临界点"""
        lookup = dict()
        for i in t:
            lookup[i] = lookup.get(i, 0) + 1

        left, right = 0, 0
        # Q1: counter = len(lookup)，那么后面的判断是lookup[s[right]] == 1，如果是len(t)那么后面的判就得改为lookup[s[r]] >= 1
        counter = len(lookup)
        start = 0
        min_len = len(s) + 1

        while right < len(s):
            if s[right] in lookup:
                # 这里的判断重点是要理解lookup中的值代表什么，1是一个临界点
                if lookup[s[right]] == 1:
                    counter -= 1
                lookup[s[right]] -= 1
            right += 1

            while counter == 0:
                if s[left] in lookup:

                    if lookup[s[left]] == 0:
                        counter += 1
                        # Q2: 为什么min_len的更新不能放在while循环外？因为求的是最小值，left在移动过程中窗口长度会越来越小，但是这些窗口是不满足条件的。
                        if min_len > right - left:
                            min_len = right - left
                            start = left
                    lookup[s[left]] += 1
                left += 1

        return s[start:start + min_len] if min_len < len(s) + 1 else ''
# leetcode submit region end(Prohibit modification and deletion)
