# 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。 
# 
#  在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums
# [k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,
# 2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。 
# 
#  给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 targ
# et ，则返回 true ，否则返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,5,6,0,0,1,2], target = 0
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,5,6,0,0,1,2], target = 3
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  -104 <= nums[i] <= 104 
#  题目数据保证 nums 在预先未知的某个下标上进行了旋转 
#  -104 <= target <= 104 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  这是 搜索旋转排序数组 的延伸题目，本题中的 nums 可能包含重复元素。 
#  这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？ 
#  
#  Related Topics 数组 二分查找 
#  👍 428 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """官方题解"""
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            # 不同之处
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:  # 左区间増序
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # 右区间増序
                if nums[mid] < target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False

    def search1(self, nums: List[int], target: int) -> bool:
        """二分查找。对比33题，多了重复元素，nums[mid] == nums[l]时无法判断左右区间谁是増序，所以将l右移一位。
        O(n)最坏的情况nums中全是同一个数字，需要遍历整个数组才能返回False。
        无重复数字则为O(log n)
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[l]:
                l += 1  # 无法判断哪个区间是増序的
            # elif nums[mid] <= nums[r]:  # 和左端右端比都可以，不过要注意不要搞反了増序区间的左右
            elif nums[mid] < nums[l]:
                # 右区间増序
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # 左区间増序
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return False

    def search2(self, nums: List[int], target: int) -> bool:
        """[0， len(nums))的搜索区间，对比search1"""
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            # 可以改成这样。注意这里不能r-=1，就像二分过程中r=mid而不是mid-1
            # if nums[mid] == nums[l] and nums[mid] == nums[r - 1]:
            #     l += 1
            # elif nums[mid] >= nums[l]:  # 注意这里是>=，即nums[mid] == nums[l]但nums[mid] != nums[r - 1]的情况
            if nums[mid] == nums[l]:
                l += 1
            elif nums[mid] > nums[l]:  # 左边有序
                if nums[mid] > target >= nums[l]:
                    r = mid
                else:
                    l = mid + 1
            else:  # 右边有序
                if nums[mid] < target <= nums[r - 1]:
                    l = mid + 1
                else:
                    r = mid

        return False


# leetcode submit region end(Prohibit modification and deletion)
"""
三种情况
nums[mid]=nums[l]: [1,1,1,2] l到mid都是同一个数，无需处理，整个区间増序
nums[mid]=nums[r]: [2,3,3,3] mid到r都是同一个数，无需处理，整个区间増序
nums[l]=nums[mid]=nums[r]: 
    [3,3,2,3] l到mid都是同一个数
    [3,2,3,3,3] mid到r都是同一个数
# Solution().search([1, 2], 2)
Solution().search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2)
# Solution().search([1, 1, 1, 1, 1, 1, 1, 1, 2], 2)
"""
