# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
# 
#  子数组是数组中元素的连续非空序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1], k = 2
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3], k = 3
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -1000 <= nums[i] <= 1000 
#  -10⁷ <= k <= 10⁷ 
#  
# 
#  Related Topics 数组 哈希表 前缀和 👍 2452 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def subarraySum1(self, nums: List[int], k: int) -> int:
        """前缀和，暴力法, 超时
        nums:   [1, 2, 3, 4]
        sums:[0, 1, 3, 6, 10] 要包含自己，所以开头这个0必须加
        """
        n = len(nums)
        ans = 0
        pre_sums = [sum(nums[:idx]) for idx in range(n + 1)]  # 注意n+1
        for i in range(n + 1):  # 注意n+1
            for j in range(i):
                if pre_sums[i] - pre_sums[j] == k:
                    ans += 1
        return ans

    def subarraySum(self, nums: List[int], k: int) -> int:
        """前缀和,hashMap"""
        pre_sum_map = dict()
        pre_sum_map[0] = 1  # bad case
        pre_sum, ans = 0, 0
        for num in nums:
            pre_sum += num
            t = pre_sum - k
            ans += pre_sum_map.get(t, 0)
            pre_sum_map[pre_sum] = pre_sum_map.get(pre_sum, 0) + 1
        return ans


Solution().subarraySum([1, 1, 1], 2)
# leetcode submit region end(Prohibit modification and deletion)
