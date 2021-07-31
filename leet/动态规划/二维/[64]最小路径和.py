# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 
# 
#  说明：每次只能向下或者向右移动一步。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 200 
#  0 <= grid[i][j] <= 100 
#  
#  Related Topics 数组 动态规划 
#  👍 856 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minPathSum2(self, grid: List[List[int]]) -> int:
        """官解评论中简洁写法"""
        dp = [float('inf')] * (len(grid[0]) + 1)
        dp[1] = 0  # 注意这一行别漏了，初始化第一次
        for row in grid:
            for idx, num in enumerate(row):
                dp[idx + 1] = min(dp[idx], dp[idx + 1]) + num
        return dp[-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        """动态规划O(m*n)+空间压缩。因为 dp 矩阵的每一个值只和左边和上面的值相关，我们可以使用空间压缩将 dp 数组压缩为 一维。
        对于第 i 行，在遍历到第 j 列的时候，因为第 j-1 列已经更新过了，所以 dp[j-1] 代表 dp[i][j-1] 的值；
        而 dp[j] 待更新，当前存储的值是在第 i-1 行的时候计算的，所以代表 dp[i-1][j] 的值。"""
        row, column = len(grid), len(grid[0])
        dp = [0] * column

        for i in range(row):
            for j in range(column):
                if i == 0 and j == 0:  # 1.1 初始化第一个值
                    dp[0] = grid[0][0]
                elif i == 0:  # 1.2 初始化第一行
                    dp[j] = dp[j - 1] + grid[0][j]
                elif j == 0:  # 1.3 初始化第一列
                    dp[0] = dp[0] + grid[i][0]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[column - 1]

    def minPathSum1(self, grid: List[List[int]]) -> int:
        """动态规划O(m*n)"""
        row, column = len(grid), len(grid[0])
        dp = [[0] * column for _ in range(row)]
        # 1.1 初始化第一个值
        dp[0][0] = grid[0][0]
        # 1.2 初始化第一列
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        # 1.3 初始化第一行
        for j in range(1, column):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        # 迭代转移方程dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        for i in range(1, row):
            for j in range(1, column):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[row - 1][column - 1]

# leetcode submit region end(Prohibit modification and deletion)
