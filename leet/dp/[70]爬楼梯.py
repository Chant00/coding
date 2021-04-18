# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  注意：给定 n 是一个正整数。 
# 
#  示例 1： 
# 
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶 
# 
#  示例 2： 
# 
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#  
#  Related Topics 动态规划 
#  👍 1608 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def MatrixMultiply(self, x, y):
        """自定义二阶矩阵乘法"""
        a = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                a[i][j] = x[i][0] * y[0][j] + x[i][1] * y[1][j]
        return a

    def MatrixQuickPow(self, x, n):
        """自定义矩阵快速幂"""
        ans = [[1, 0], [0, 1]]
        while n > 0:
            if n & 1:
                ans = self.MatrixMultiply(ans, x)
            x = self.MatrixMultiply(x, x)
            n >>= 1
        return ans

    def climbStairs(self, n: int) -> int:
        """矩阵快速幂O(log(n))"""
        return self.MatrixQuickPow([[1, 1], [1, 0]], n)[0][0]

    def climbStairs3(self, n: int) -> int:
        """通项公式O(math.pow)"""
        sqrt5 = math.sqrt(5)
        n = n + 1  # n阶楼梯对应的是斐波那契数列的n+1项
        return int((math.pow((1 + sqrt5) / 2, n) - math.pow((1 - sqrt5) / 2, n)) / sqrt5)

    def climbStairs1(self, n: int) -> int:
        """动态规划O(n)"""
        if n <= 2:
            return n
        pre1, pre2 = 1, 2
        ret = 0
        for i in range(2, n):
            ret = pre1 + pre2
            pre1 = pre2
            pre2 = ret
        return ret
# leetcode submit region end(Prohibit modification and deletion)
