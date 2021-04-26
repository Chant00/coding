# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。 
# 
#  
#  '.' 匹配任意单个字符 
#  '*' 匹配零个或多个前面的那一个元素 
#  
# 
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aa" p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2: 
# 
#  
# 输入：s = "aa" p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "ab" p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "aab" p = "c*a*b"
# 输出：true
# 解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#  
# 
#  示例 5： 
# 
#  
# 输入：s = "mississippi" p = "mis*is*p*."
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 20 
#  0 <= p.length <= 30 
#  s 可能为空，且只包含从 a-z 的小写字母。 
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。 
#  保证每次出现字符 * 时，前面都匹配到有效的字符 
#  
#  Related Topics 字符串 动态规划 回溯算法 
#  👍 2061 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch1(self, s: str, p: str) -> bool:
        """官方"""
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]

    def isMatch(self, s: str, p: str) -> bool:
        """
        dp[i][j] 表示以 i 截止的字符串是否可以被以 j 截止的 正则表达式匹配
        字符、星号，点号，我们可以分情况讨论来更 新 dp 数组
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # s和p都为空字符串时True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] != '*':
                    # dp[i][j] = dp[i - 1][j - 1] and p[j - 1] == s[i - 1]
                    if p[j - 1] == s[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 2] != s[i - 1] and p[j - 2] != '.':
                    dp[i][j] = dp[i][j - 2]
                else:
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j] or dp[i][j - 2]

        return dp[m][n]

# leetcode submit region end(Prohibit modification and deletion)
