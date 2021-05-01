# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变
# 化后可能得到：
#  
#  若旋转 4 次，则可以得到 [4,5,6,7,0,1,4] 
#  若旋转 7 次，则可以得到 [0,1,4,4,5,6,7] 
#  
# 
#  注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], 
# ..., a[n-2]] 。 
# 
#  给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,3,5]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,2,0,1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 5000 
#  -5000 <= nums[i] <= 5000 
#  nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  这道题是 寻找旋转排序数组中的最小值 的延伸题目。 
#  允许重复会影响算法的时间复杂度吗？会如何影响，为什么？ 
#  
#  Related Topics 数组 二分查找 
#  👍 356 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """这道题比较特殊，很多细节，nums[mid]只能通过和nums[r]比较来确定最小值在mid的左边还是右边，
        如果和nums[l]做比较，会有问题，比如：nums[mid] > nums[l]，
        如果nums[l]和真实最小值是两个升序子数组各自的最小值，最小值在mid的右边
        但是如果整个数组没有旋转，完全升序，那么此时nums[l]就是最小值，此时最小值在mid的左边
        """
        l, r = 0, len(nums) - 1  # 不能令r=len(nums)，因为后面会取nums[r]来比较大小，数组越界
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid  # 因为nums[mid]可能是最小值，所以不能像正常二分查找那样令r=mid-1
            elif nums[mid] > nums[r]:
                l = mid + 1  # nums[mid] > nums[r], 自然不可能是最小值
            else:
                r -= 1
        return nums[l]
# leetcode submit region end(Prohibit modification and deletion)
