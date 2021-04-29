# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  进阶： 
# 
#  
#  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 105 
#  -109 <= nums[i] <= 109 
#  nums 是一个非递减数组 
#  -109 <= target <= 109 
#  
#  Related Topics 数组 二分查找 
#  👍 973 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def binarySearch(self, nums, target, lower):
        l, r = 0, len(nums) - 1
        ans = len(nums)
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target or (lower and nums[mid] >= target):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False) - 1
        if left <= right < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        else:
            return [-1, -1]
# leetcode submit region end(Prohibit modification and deletion)


# Solution().binarySearch([5, 6, 7, 7, 8, 8, 10], 8, True)
# Solution().binarySearch([5, 6, 7, 7, 8, 8, 10], 8, False)
