# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "a"
# 输出："a"
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "ac"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母（大写和/或小写）组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 3536 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome1(self, s: str) -> str:
        """动态规划O(n^2)"""
        n = len(s)
        if n < 2:
            return s
        dp = [[False] * n for _ in range(n)]

        max_len = 1
        start = 0
        for L in range(2, n + 1):
            for i in range(n):
                j = L - 1 + i
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and max_len < L:
                    start, max_len = i, L
        return s[start:start + max_len]

    def expand_center(self, s, l, r, res):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        if res[1] - res[0] < r - (l + 1):
            res[0], res[1] = l + 1, r

    def longestPalindrome2(self, s: str) -> str:
        """中心扩展算法，代码简洁版O(n^2)"""
        res = [0, 1]
        for i in range(len(s)):
            self.expand_center(s, i, i, res)
            self.expand_center(s, i, i + 1, res)
        return s[res[0]:res[1]]

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        """马拉车算法O(n) =中心扩展+动态规划"""
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'  # 使字符串长度变为奇数
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                if arm_len[i_sym] < right - i:
                    cur_arm_len = arm_len[i_sym]
                elif arm_len[i_sym] == right - i:
                    cur_arm_len = self.expand(s, i - arm_len[i_sym], i + arm_len[i_sym])
                else:
                    cur_arm_len = right - i
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start + 1:end + 1:2]
# leetcode submit region end(Prohibit modification and deletion)
