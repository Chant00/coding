# 整数数组 nums 按升序排列，数组中的值 互不相同 。 
# 
#  在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[
# k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2
# ,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。 
# 
#  给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1], target = 0
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  -10^4 <= nums[i] <= 10^4 
#  nums 中的每个值都 独一无二 
#  题目数据保证 nums 在预先未知的某个下标上进行了旋转 
#  -10^4 <= target <= 10^4 
#  
# 
#  
# 
#  进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？ 
#  Related Topics 数组 二分查找 
#  👍 1344 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
    此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环.
    """

    def search(self, nums: List[int], target: int) -> int:
        """[]的方式搜索，所以r=len(nums)-1, while l<= r，r = mid -1"""
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            # 当mid就是0的时候，显然[0,mid]是有序的(只有一个元素)，应该走if分支
            if nums[l] <= nums[mid]:  # 注意：这里一定是<=，<是错误的
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    def search2(self, nums: List[int], target: int) -> int:
        """[)的方式搜索，所以r=len(nums), while l<r，r = mid"""
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[mid]:  # 注意：这里是<或<=都可以，因为r=len(nums)，所以规避了mid就是0的情况
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r - 1]:
                    l = mid + 1
                else:
                    r = mid
        return -1

    def search3(self, nums: List[int], target: int) -> int:
        """官方题解版，有些许不同"""
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:  # 注意:这里不是nums[l] <= nums[mid]
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:  # 注意:这里不是target <= nums[r]
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


# Solution().search([4, 5, 6, 7, 0, 1, 2], 3)
# Solution().search([1], 1)
Solution().search2([3, 1], 1)
# leetcode submit region end(Prohibit modification and deletion)
