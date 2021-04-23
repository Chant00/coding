# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。 
# 
#  
#  请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。 
# 
#  如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 
# n 的值 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= strs.length <= 600 
#  1 <= strs[i].length <= 100 
#  strs[i] 仅由 '0' 和 '1' 组成 
#  1 <= m, n <= 100 
#  
#  Related Topics 动态规划 
#  👍 378 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def count_zeros_ones(self, s):
        cnt0, cnt1 = 0, 0
        for c in s:
            if c == '0':
                cnt0 += 1
            else:
                cnt1 += 1
        return cnt0, cnt1

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """我们用 dp(i, j) 表示使用 i 个 0 和 j 个 1，最多能拼出的字符串数目。
        状态转移方程为dp[i][j] = max(dp[i][j], dp[i - cnt0][j - cnt1] + 1)
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            cnt0, cnt1 = self.count_zeros_ones(s)
            for i in range(m, cnt0 - 1, -1):
                for j in range(n, cnt1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - cnt0][j - cnt1] + 1)
        return dp[m][n]
# leetcode submit region end(Prohibit modification and deletion)
