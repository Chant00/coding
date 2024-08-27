# 给你一个整数数组 nums 和一个整数 k ，如果 nums 有一个 好的子数组 返回 true ，否则返回 false： 
# 
#  一个 好的子数组 是： 
# 
#  
#  长度 至少为 2 ，且 
#  子数组元素总和为 k 的倍数。 
#  
# 
#  注意： 
# 
#  
#  子数组 是数组中 连续 的部分。 
#  如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终 视为 k 的一个倍数。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [23,2,4,6,7], k = 6
# 输出：true
# 解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [23,2,6,4,7], k = 6
# 输出：true
# 解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。 
# 42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [23,2,6,4,7], k = 13
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  0 <= nums[i] <= 10⁹ 
#  0 <= sum(nums[i]) <= 2³¹ - 1 
#  1 <= k <= 2³¹ - 1 
#  
# 
#  Related Topics 数组 哈希表 数学 前缀和 👍 583 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        前缀和+哈希表，在哈希表中存储下标，然后i-j>1判断
        当 prefixSums[q]−prefixSums[p] 为 k 的倍数时，prefixSums[p] 和 prefixSums[q] 除以 k 的余数相同。
        """
        map = {0: -1}
        s = 0
        for i, num in enumerate(nums):
            s += num
            remainder = s % k
            if remainder in map:
                if i - map[remainder] > 1:
                    return True
                map[remainder] = min(i, map.get(remainder))
            else:
                map[remainder] = i
        return False

    def checkSubarraySum1(self, nums: List[int], k: int) -> bool:
        """极简版
        前缀和+哈希表，鉴于这里只要求长度至少为2，因此前缀和延迟一步计入集合即可：
        当 prefixSums[q]−prefixSums[p] 为 k 的倍数时，prefixSums[p] 和 prefixSums[q] 除以 k 的余数相同。
        """
        seen = {0}
        pre_sum = nums[0]
        for num in nums[1:]:  # 注意从1开始
            cur_sum = pre_sum + num
            if cur_sum % k in seen:
                return True
            seen.add(pre_sum % k)  # 前缀和延迟一步计入集合
            pre_sum = cur_sum
        return False

    def checkSubarraySum0(self, nums: List[int], k: int) -> bool:
        """前缀和，暴力法，超时"""
        pre_sums = [0]
        pre_sum = 0
        for i, num in enumerate(nums):
            pre_sum += num
            # for j, s in enumerate(pre_sums):
            #     if (pre_sum - pre_sums[j]) % k == 0 and i - j > 0:
            # 这样写，可以省去i - j > 0的判断
            for j in range(i):
                if (pre_sum - pre_sums[j]) % k == 0:
                    return True
            pre_sums.append(pre_sum)
        return False

# print(Solution().checkSubarraySum([2, 4, 3], 6))
# print(Solution().checkSubarraySum([0], 1))
# leetcode submit region end(Prohibit modification and deletion)
