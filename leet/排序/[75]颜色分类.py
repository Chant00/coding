# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。 
# 
#  此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[0]
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [1]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 300 
#  nums[i] 为 0、1 或 2 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你可以不使用代码库中的排序函数来解决这道题吗？ 
#  你能想出一个仅使用常数空间的一趟扫描算法吗？ 
#  
#  Related Topics 排序 数组 双指针 
#  👍 874 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """把每种if都写出来，最容易理解"""
        p1, p2 = 0, len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
                i += 1
            elif nums[i] == 1:  # 注意是elif，容易少了else导致有问题
                i += 1
            elif nums[i] == 2:
                # 需要注意从后面交换到中间的数字有可能是0，需要再判断一次。所以没有i+=1
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1

    def sortColors(self, nums: List[int]) -> None:
        """
        双指针法，把0交换到前面，把2交换到后面。
        需要注意从后面交换到中间的数字有可能是0，需要再判断一次。
        """
        p1, p2 = 0, len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1

    def sortColors(self, nums: List[int]) -> None:
        """三路快排，直接分为< = >三个部分"""
        p0, p2 = 0, len(nums) - 1
        i = 0
        while i <= p2:
            # 顺序不能反，必须先和后面比，再和前面比。
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1

    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = p1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1


# leetcode submit region end(Prohibit modification and deletion)
Solution().sortColors([2, 0, 2, 1, 1, 0])
