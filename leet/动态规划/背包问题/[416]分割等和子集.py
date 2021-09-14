# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
#  Related Topics 动态规划 
#  👍 755 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """其中 dp[i][j] 表示 从数组的 [0,i] 下标范围内选取若干个正整数（可以是 0 个）, 每个数只能用一次，能否使得这些数的和等于 j"""
        target, remainder = divmod(sum(nums), 2)
        if remainder == 1:
            return False

        dp = [True] + [False] * target  # 如果不选取任何正整数，则被选取的正整数等于 0，所以为True。 
        for i in range(1, len(nums) + 1):
            for j in range(target, nums[i - 1] - 1, -1):  # 倒序遍历，否则dp[j]就被dp[i][j]覆盖了，不再是dp[i-1][j]
                # dp[j] = dp[j] or dp[j - nums[i - 1]]
                if dp[j - nums[i - 1]]:
                    dp[j] = True
        return dp[target]

# leetcode submit region end(Prohibit modification and deletion)
