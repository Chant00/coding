# 最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作： 
# 
#  
#  Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。 
#  Paste (粘贴) : 你可以粘贴你上一次复制的字符。 
#  
# 
#  给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。 
# 
#  示例 1: 
# 
#  
# 输入: 3
# 输出: 3
# 解释:
# 最初, 我们只有一个字符 'A'。
# 第 1 步, 我们使用 Copy All 操作。
# 第 2 步, 我们使用 Paste 操作来获得 'AA'。
# 第 3 步, 我们使用 Paste 操作来获得 'AAA'。
#  
# 
#  说明: 
# 
#  
#  n 的取值范围是 [1, 1000] 。 
#  
#  Related Topics 动态规划 
#  👍 276 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def minSteps(self, n: int) -> int:
        """动态规划 不同于其它动态规划题目的加减法来递推，本题用乘除法来递推
        dp[i]表示得到i个A所需要的操作数，则我们的目的是求dp[n]
        状态转移方程：dp[i] = dp[j] + dp[i/j] （j是一个小于i的数，且能被i整除，其实就是i的因数，注意把j==1的情况排除掉）
        说明：上述方程对应了前面介绍的规律，dp[6] = dp[2] + dp[3]
        初始化：dp[i] = i （表示一个A一个A的粘贴，是实现步骤最多的方法）
        这里的j不需要写成j <= i，因为判断j是不是因数只要检查到开平方的大小就好了，算是个小优化
        """
        dp = [0] * (n + 1)
        sqrt_n = int(math.sqrt(n))
        for i in range(2, n + 1):
            dp[i] = i
            for j in range(2, sqrt_n + 1):
                quotient, remainder = divmod(i, j)
                if remainder == 0:
                    dp[i] = dp[j] + dp[quotient]
                    break
        return dp[n]

    def minSteps1(self, n: int) -> int:
        """素数分解 O(sqrt(N)) 当 N 是素数的平方时，需要循环 O(sqrt(N)) 步"""
        ans, d = 0, 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
