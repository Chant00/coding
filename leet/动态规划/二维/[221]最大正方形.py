# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 300 
#  matrix[i][j] 为 '0' 或 '1' 
#  
#  Related Topics 动态规划 
#  👍 743 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """用原数组存算出来的值，空间复杂度是不是就降到O(1)"""
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return 0

        max_side = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
                else:
                    if i == 0 or j == 0:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) + 1
                    max_side = max(max_side, matrix[i][j])
        return max_side ** 2

    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        """O(m*n)对于在矩阵内搜索正方形或长方形的题型，一种常见的做法是定义一个二维 dp 数组，
        其中 dp[i][j] 表示满足题目条件的、以 (i, j) 为右下角的正方形或者长方形的属性。
        对于本题，则表示 以 (i, j) 为右下角的全由 1 构成的最大正方形边长，用面积会很复杂。
            1. 如果当前位置是 0，那么 dp[i][j] 即为 0；
            2. 如果 当前位置是 1，我们假设 dp[i][j] = k，
            其充分条件为 dp[i-1][j-1]、dp[i][j-1] 和 dp[i-1][j] 的值必须 都不小于 (k − 1)，
            否则 (i, j) 位置不可以构成一个边长为 k 的正方形。
            所以，状态转移方程为: dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1
        如果读者对这个状态转移方程感到不解，可以参考 1277. 统计全为 1 的正方形子矩阵的官方题解，其中给出了详细的证明。
        此外，还需要考虑边界条件。如果 i 和 j 中至少有一个为 0，则以位置 (i, j)(i,j) 为右下角的最大正方形的边长只能是 1，此时dp(i,j)=1。
        """
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return 0

        max_side = 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side ** 2
# leetcode submit region end(Prohibit modification and deletion)
