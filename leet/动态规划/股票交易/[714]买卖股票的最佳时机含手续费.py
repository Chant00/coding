# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。 
# 
#  你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。 
# 
#  返回获得利润的最大值。 
# 
#  注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。 
# 
#  示例 1: 
# 
#  输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:  
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8. 
# 
#  注意: 
# 
#  
#  0 < prices.length <= 50000. 
#  0 < prices[i] < 50000. 
#  0 <= fee < 50000. 
#  
#  Related Topics 贪心算法 数组 动态规划 
#  👍 460 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProfit_wrong(self, prices: List[int], fee: int) -> int:
        # dp0手里没有股票时的最大收益，dp1手里有1支股票的最大收益
        dp0, dp1 = 0, 0
        for price in prices:
            dp0 = max(dp0, dp1 + price - fee)  # 这里应该是有问题的，但是居然能AC，莫非是测试里的fee都比prices[0]大？
            dp1 = max(dp1, dp0 - price)
        return dp0

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp0, dp1 = 0, -prices[0]  # dp0手里没有股票时的最大收益，dp1手里有1支股票的最大收益
        for i in range(1, n):
            dp0 = max(dp0, dp1 + prices[i] - fee)
            dp1 = max(dp1, dp0 - prices[i])
        return dp0
# leetcode submit region end(Prohibit modification and deletion)
