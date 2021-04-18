# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上
# 被小偷闯入，系统会自动报警。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。 
# 
#  示例 2： 
# 
#  输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 100 
#  0 <= nums[i] <= 400 
#  
#  Related Topics 动态规划 
#  👍 1410 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        定义一个数组 dp，dp[i] 表示抢劫到第 i 个房子时，可以抢劫的最大数量。我们考虑 dp[i]， 此时可以抢劫的最大数量有两种可能，
        一种是我们选择不抢劫这个房子，此时累计的金额即为 dp[i-1]；另一种是我们选择抢劫这个房子，那么此前累计的最大金额只能是 dp[i-2]，
        因为我们不 能够抢劫第 i-1 个房子，否则会触发警报机关。因此本题的状态转移方程为 dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])。
        """
        # dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
        if len(nums) == 0:
            return 0
        prev1, prev2 = 0, 0
        for i in nums:
            ans = max(prev1, prev2 + i)
            prev2 = prev1
            prev1 = ans
        return ans
# leetcode submit region end(Prohibit modification and deletion)
