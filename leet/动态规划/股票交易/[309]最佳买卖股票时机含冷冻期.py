# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。 
# 
#  设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）: 
# 
#  
#  你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
#  卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。 
#  
# 
#  示例: 
# 
#  输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出] 
#  Related Topics 动态规划 
#  👍 757 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """空间优化
        注意到上面的状态转移方程中，f[i][..] 只与 f[i-1][..] 有关，而与 f[i-2][..] 及之前的所有状态都无关，
        因此我们不必存储这些无关的状态。也就是说，我们只需要将 f[i-1][0]，f[i-1][1]，f[i-1][2] 存放在三个变量中，
        通过它们计算出 f[i][0]，f[i][1]，f[i][2] 并存回对应的变量，以便于第 i+1 天的状态转移即可。
        """
        n = len(prices)
        # dp0 手上持有股票的最大收益
        # dp1 手上不持有股票，并且处于冷冻期中的累计最大收益
        # dp2 手上不持有股票，并且不在冷冻期中的累计最大收益
        dp0, dp1, dp2 = -prices[0], 0, 0
        for i in range(n):
            cur_dp1 = dp0 + prices[i]  # 注意顺序，否则得写三个临时变量
            dp0 = max(dp0, dp2 - prices[i])
            dp2 = max(dp1, dp2)
            dp1 = cur_dp1
        return max(dp1, dp2)

    def maxProfit11(self, prices: List[int]) -> int:
        """动态规划,对比maxProfit1，dp 长度初始化为 n+1"""
        n = len(prices)
        # dp[i][0] 手上持有股票的最大收益
        # dp[i][1] 手上不持有股票，并且处于冷冻期中的累计最大收益
        # dp[i][2] 手上不持有股票，并且不在冷冻期中的累计最大收益
        dp = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n)]

        for i in range(1, n + 1):
            # print('i: ', i)
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i - 1])
            dp[i][1] = dp[i - 1][0] + prices[i - 1]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])

        return max(dp[n][1], dp[n][2])

    def maxProfit1(self, prices: List[int]) -> int:
        """动态规划"""
        n = len(prices)
        # dp[i][0] 手上持有股票的最大收益
        # dp[i][1] 手上不持有股票，并且处于冷冻期中的累计最大收益
        # dp[i][2] 手上不持有股票，并且不在冷冻期中的累计最大收益
        dp = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])

        return max(dp[n - 1][1], dp[n - 1][2])
# leetcode submit region end(Prohibit modification and deletion)
