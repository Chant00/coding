# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。 
# 
#  
# 
#  进阶： 
# 
#  
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。 
#  你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？ 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#  
# 
#  示例 2: 
# 
#  
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 104 
#  -231 <= nums[i] <= 231 - 1 
#  0 <= k <= 105 
#  
# 
#  
#  
#  Related Topics 数组 数学 双指针 
#  👍 1043 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.rotate2(nums, k)

    def gcd(self, a, b):
        """最大公约数，辗转相除法"""
        while a != 0:
            a, b = b % a, a  # 如果a>b,第一轮循环就会将a、b交换，所以不用去比较大小
        return b

    def rotate2(self, nums: List[int], k: int) -> None:
        """官解方法2：环状替换，不好理解，记不住"""
        n = len(nums)
        k = k % n
        for i in range(self.gcd(k, n)):  # 需要执行最大公约数次
            cur, pre = i, nums[i]

            while True:
                next = (cur + k) % n
                nums[next], pre, cur = pre, nums[next], next
                if cur == i:  # 这样写相当于c和java中的do{}while()，保证至少先执行一遍
                    break

    def reverse(self, nums: List[int], start, end):
        l, r = start, end
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate3(self, nums: List[int], k: int) -> None:
        """官解方法3: 先反转数组，再把两个子数组再各自反转。记住这种，比较好理解"""
        n = len(nums)
        k = k % n  # 这一步别忘了，k可能会大于len(nums)，取模省去不必要的重复旋转
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)  # 注意这里的k-1，以及另外的n-1边界问题
        self.reverse(nums, k, n - 1)

    def rotate1(self, nums: List[int], k: int) -> None:
        """切片"""
        # 注释里这种方式会Time Limit Exceeded
        # k = k % len(nums)
        # for _ in range(k):
        #     num = nums.pop()
        #     nums[:] = [num] + nums
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
# leetcode submit region end(Prohibit modification and deletion)
