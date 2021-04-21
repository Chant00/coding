# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。 
# 
#  两个相邻元素间的距离为 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# 
# 输出：
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#  
# 
#  示例 2： 
# 
#  
# 输入：
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
# 
# 输出：
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定矩阵的元素个数不超过 10000。 
#  给定矩阵中至少有一个元素是 0。 
#  矩阵中的元素只在四个方向上相邻: 上、下、左、右。 
#  
#  Related Topics 深度优先搜索 广度优先搜索 
#  👍 412 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """相当于是 [821]字符的最短距离 的二维版本
        一般来说，因为这道题涉及到四个方向上的最近搜索，所以很多人的第一反应可能会是广度 优先搜索。
        但是对于一个大小 O(mn) 的二维数组，对每个位置进行四向搜索，最坏情况的时间复 杂度（即全是 1）会达到恐怖的 O(m^2*n^2 )。
        一种办法是使用一个 dp 数组做 memoization，使得广 度优先搜索不会重复遍历相同位置；另一种更简单的方法是，
        我们从左上到右下进行一次动态搜 索，再从右下到左上进行一次动态搜索。两次动态搜索即可完成四个方向上的查找。"""
        m, n = len(matrix), len(matrix[0])
        dp = [[float('inf')] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i < m - 1:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                    if j < n - 1:
                        dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp
# leetcode submit region end(Prohibit modification and deletion)
