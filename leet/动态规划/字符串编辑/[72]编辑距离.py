# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。 
# 
#  你可以对一个单词进行如下三种操作： 
# 
#  
#  插入一个字符 
#  删除一个字符 
#  替换一个字符 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#  
# 
#  示例 2： 
# 
#  
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= word1.length, word2.length <= 500 
#  word1 和 word2 由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 1565 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """类似于题目 1143，我们使用一个二维数组 dp[i][j]，表示将第一个字符串到位置 i 为止，
        和第 二个字符串到位置 j 为止，最多需要几步编辑。
        当第 i 位和第 j 位对应的字符相同时，
            dp[i][j] 等于 dp[i-1][j-1]；
        当二者对应的字符不同时， 
            修改的消耗是 dp[i-1][j-1]+1，
            插入 i 位置/删除 j 位置的消耗是 dp[i][j-1] + 1， （对单词 B 删除一个字符和对单词 A 插入一个字符也是等价的）
            插入 j 位置/删除 i 位置的消耗是 dp[i-1][j] + 1。 （单词 A 删除一个字符和对单词 B 插入一个字符是等价的）
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if i == 0:  # word1为空字符串
                    dp[i][j] = j
                elif j == 0:  # word2为空字符串
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1)

        return dp[m][n]
# leetcode submit region end(Prohibit modification and deletion)
