# 如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。 
# 
#  例如，以下数列为等差数列: 
# 
#  
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9 
# 
#  以下数列不是等差数列。 
# 
#  
# 1, 1, 2, 5, 7 
# 
#  
# 
#  数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。 
# 
#  如果满足以下条件，则称子数组(P, Q)为等差数组： 
# 
#  元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。 
# 
#  函数要返回数组 A 中所有为等差数组的子数组个数。 
# 
#  
# 
#  示例: 
# 
#  
# A = [1, 2, 3, 4]
# 
# 返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。
#  
#  Related Topics 数学 动态规划 
#  👍 231 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        这道题略微特殊，因为要求是等差数列，可以很自然的想到子数组必定满足 num[i] - num[i-1] = num[i-1] - num[i-2]。
        然而由于我们对于 dp 数组的定义通常为以 i 结尾的，满足某些条件的子数 组数量，
        而等差子数组可以在任意一个位置终结，因此此题在最后需要对 dp 数组求和。
        """
        # dp[i]记录的是以nums[i]结尾的等差数列个数，dp[i]=dp[i-1]+1。
        # 如nums=[1,2,3,4,5]以nums[3]=4结尾的有[[2,3,4],[1,2,3,4]]，则以nums[4]=5结尾的有[[2,3,4,5],[1,2,3,4,5],[3,4,5]]，只多一个
        dp = 0
        ans = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp += 1
                ans += dp
            else:
                dp = 0
        return ans
# leetcode submit region end(Prohibit modification and deletion)
