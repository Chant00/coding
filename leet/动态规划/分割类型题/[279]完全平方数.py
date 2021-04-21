# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。 
# 
#  给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。 
# 
#  完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4 
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 104 
#  
#  Related Topics 广度优先搜索 数学 动态规划 
#  👍 836 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def numSquares(self, n: int) -> int:
        """对于分割类型题，动态规划的状态转移方程通常并不依赖相邻的位置，而是依赖于满足分割 条件的位置。
        我们定义一个一维矩阵 dp，其中 dp[i] 表示数字 i 最少可以由几个完全平方数相加 构成。
        在本题中，位置 i 只依赖 i - k 2 的位置，如 i - 1、i - 4、i - 9 等等，才能满足完全平方分割 的条件。
        因此 dp[i] 可以取的最小值即为 1 + min(dp[i-1], dp[i-4], dp[i-9] · · · )。"""
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        # 避免重复计算k的平方
        square_nums = [i ** 2 for i in range(int(math.sqrt(n) + 1))]
        for i in range(1, n + 1):
            for square in square_nums:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]
# leetcode submit region end(Prohibit modification and deletion)
