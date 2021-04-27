# 给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。 
# 
#  我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [4,2,3]
# 输出: true
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [4,2,1]
# 输出: false
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10 ^ 4 
#  - 10 ^ 5 <= nums[i] <= 10 ^ 5 
#  
#  Related Topics 数组 
#  👍 571 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def checkPossibility(self, nums):
        """标记修改次数的代码，可以进一步解决k次修改的问题
        遍历数组，如果遇到递减：
            还能修改：
                修改方案1：将nums[i]缩小至nums[i + 1]；
                修改方案2：将nums[i + 1]放大至nums[i]；
            第二次遇到递减，不能修改了：直接返回false；
        """
        n = len(nums)
        count = 0  # 标识修改次数
        for i in range(1, n):
            if nums[i] < nums[i - 1]:  # 出现递减
                count += 1
                if count >= 1:
                    return False
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return count <= 1

    def checkPossibility2(self, nums: List[int]) -> bool:
        """简化代码"""
        flag = True  # 标识是否还能修改
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:  # 要么缩小nums[i]，要么放大nums[i+1]
                if flag:  # 如果还有修改机会，进行修改
                    # 注意i == 0的特殊情况
                    if i == 0 or nums[i + 1] >= nums[i - 1]:
                        nums[i] = nums[i + 1]  # 缩小nums[i]，因为nums[i+1]比nums[i-1]大
                    else:
                        nums[i + 1] = nums[i]  # 放大nums[i+1]，因为nums[i+1]太小了比nums[i-1]还小
                    flag = False  # 用掉唯一的修改机会
                else:  # 没有修改机会，直接结束
                    return False
        return True

    def checkPossibility1(self, nums: List[int]) -> bool:
        """
        遍历数组，如果遇到递减：
            还能修改：
                修改方案1：将nums[i]缩小至nums[i + 1]；
                修改方案2：将nums[i + 1]放大至nums[i]；
            修改后第二次遇到递减，不能修改了：直接返回false；
        """
        if len(nums) == 1: return True
        flag = nums[0] <= nums[1]  # 标识是否还能修改
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i + 1]:  # 要么缩小nums[i]，要么放大nums[i+1]
                if flag:  # 如果还有修改机会，进行修改
                    if nums[i + 1] >= nums[i - 1]:
                        nums[i] = nums[i + 1]  # 缩小nums[i]，因为nums[i+1]比nums[i-1]大
                    else:
                        nums[i + 1] = nums[i]  # 放大nums[i+1]，因为nums[i+1]太小了比nums[i-1]还小
                    flag = False  # 用掉唯一的修改机会
                else:  # 没有修改机会，直接结束
                    return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
