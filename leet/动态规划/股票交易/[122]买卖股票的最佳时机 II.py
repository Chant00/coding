# 给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。 
# 
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: prices = [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#  
# 
#  示例 2: 
# 
#  
# 输入: prices = [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#  
# 
#  示例 3: 
# 
#  
# 输入: prices = [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 3 * 104 
#  0 <= prices[i] <= 104 
#  
#  Related Topics 贪心算法 数组 
#  👍 1198 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """贪心算法O(n),空间O(1)
        需要说明的是，贪心算法只能用于计算最大利润，计算的过程并不是实际的交易过程。
        """
        ans = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i] - prices[i - 1])
        return ans

    def maxProfit3(self, prices: List[int]) -> int:
        """动态规划O(n)，空间O(1)，空间优化，循环中其实无需临时变量"""
        dp0, dp1 = 0, -prices[0]  # dp0手里没有股票时的最大收益，dp1手里有1支股票的最大收益
        n = len(prices)
        for i in range(1, n):
            # dp0如果改变取 dp1 + prices[i]，那么dp1必然只能取dp1，两者互斥
            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, dp0 - prices[i])
        return dp0

    def maxProfit2(self, prices: List[int]) -> int:
        """动态规划O(n)，空间O(1)，空间优化"""
        dp0, dp1 = 0, -prices[0]  # dp0手里没有股票时的最大收益，dp1手里有1支股票的最大收益
        n = len(prices)
        for i in range(1, n):
            cur_dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, dp0 - prices[i])
            dp0 = cur_dp0
        return dp0

    def maxProfit1(self, prices: List[int]) -> int:
        """动态规划O(n)，空间O(n)，定义状态 dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润，
        dp[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润（i 从 0 开始）
        """
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            # 昨天没股票dp[i - 1][0]，昨天有股票今天卖掉dp[i - 1][1] + prices[i]
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # 昨天有股票dp[i - 1][0]，昨天没股票今天买一份dp[i - 1][1] - prices[i]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

# leetcode submit region end(Prohibit modification and deletion)
