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
#  👍 977 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


def binarySearch(nums, target, lower):
    l, r = 0, len(nums) - 1
    ans = len(nums)
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] > target or (lower and nums[mid] == target):
            r = mid - 1
            ans = mid  # Q: 为什么只能在nums[mid] > target中更新ans？
        else:
            l = mid + 1
    return ans


def binarySearch2(nums, target, lower, l, r):
    ans = len(nums)
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] > target or (lower and nums[mid] == target):
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    return ans


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """官方题解，二分法，左右边界都找"""
        left = binarySearch(nums, target, True)
        right = binarySearch(nums, target, False) - 1
        if left <= right < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        else:
            return [-1, -1]

    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        """先找左边界，有左边界再找右边界"""
        left = binarySearch(nums, target, True)
        if not (left < len(nums) and nums[left] == target):
            return [-1, -1]

        right = binarySearch(nums, target, False) - 1
        return [left, right]

    def searchRange3(self, nums: List[int], target: int) -> List[int]:
        """二分法找到左边界后，在左边界之后的片段中二分找右边界"""
        left = binarySearch2(nums, target, True, 0, len(nums) - 1)
        if not (left < len(nums) and nums[left] == target):
            return [-1, -1]

        right = binarySearch2(nums, target, False, left, len(nums) - 1) - 1
        return [left, right]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        """二分法找到左边界后，左边界基础上继续往右找右边界,
        问题在于极端情况下复杂度是O(n), 比如nums中数字全是target, 所以还是应该用二分法找右边界
        不过这里（如何继续沿着后面寻找右边界）依旧值得学习，while循环一步步往后走，不用处理任何边界条件
        """
        left = binarySearch(nums, target, True)

        if not (left < len(nums) and nums[left] == target):
            return [-1, -1]

        right = left
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
        return [left, right]
# leetcode submit region end(Prohibit modification and deletion)
