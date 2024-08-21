# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。 
# 
#  你可以假设数组中无重复元素。 
# 
#  示例 1: 
# 
#  输入: [1,3,5,6], 5
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [1,3,5,6], 2
# 输出: 1
#  
# 
#  示例 3: 
# 
#  输入: [1,3,5,6], 7
# 输出: 4
#  
# 
#  示例 4: 
# 
#  输入: [1,3,5,6], 0
# 输出: 0
#  
#  Related Topics 数组 二分查找 
#  👍 895 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """二分查找，找到满足nums[i]<=target的最大i"""
        l, r = 0, len(nums) - 1
        # loc = len(nums)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                # loc = mid
                r = mid - 1
            else:
                l = mid + 1
        return l

    def searchInsert1_1(self, nums: List[int], target: int) -> int:
        """二分查找，找到满足nums[i]<=target的最大i"""
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
        return l

    def searchInsert1(self, nums: List[int], target: int) -> int:
        """二分查找，找到满足nums[i]<=target的最大i"""
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                r = mid
            elif nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
        return l

    def searchInsert0(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                l = mid
                break
            elif nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
        return l
# leetcode submit region end(Prohibit modification and deletion)
