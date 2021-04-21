# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。 
# 
#  子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序
# 列。 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2500 
#  -104 <= nums[i] <= 104 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你可以设计时间复杂度为 O(n2) 的解决方案吗？ 
#  你能将算法的时间复杂度降低到 O(n log(n)) 吗? 
#  
#  Related Topics 二分查找 动态规划 
#  👍 1543 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """O(n*log(n))贪心+二分查找"""
        n = len(nums)
        dp = [nums[0]]
        for i in range(1, n):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                # 二分查找 找到第 1 个大于等于 nums[i] 的元素，尝试让那个元素更小
                l, r = 0, len(dp) - 1
                while l < r:
                    mid = (l + r) >> 1
                    # 选左中位数不是偶然，而是有原因的，原因请见 LeetCode 第 35 题题解
                    if dp[mid] < nums[i]:
                        l = mid + 1  # 中位数肯定不是要找的数，把它写在分支的前面
                    else:
                        r = mid
                # 走到这里是因为【逻辑 1】的反面，因此一定能找到第 1 个大于等于 nums[i] 的元素，因此无需再单独判断
                dp[l] = nums[i]
        return len(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)

    def lengthOfLIS1(self, nums: List[int]) -> int:
        """在本题中，dp[i] 可以表示以 i 结尾的、最长子序列长度。
        对于每一个位置 i，如果其之前的某 个位置 j 所对应的数字小于位置 i 所对应的数字，
        则我们可以获得一个以 i 结尾的、长度为 dp[j] + 1 的子序列。
        为了遍历所有情况，我们需要 i 和 j 进行两层循环，其时间复杂度为 O(n^2)。
        """
        n = len(nums)
        dp = [1] * n
        max_len = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_len = max(max_len, dp[i])
        return max_len
# leetcode submit region end(Prohibit modification and deletion)
