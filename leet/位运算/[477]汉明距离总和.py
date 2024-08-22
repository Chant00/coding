# 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。 
# 
#  给你一个整数数组 nums，请你计算并返回 nums 中任意两个数之间 汉明距离的总和 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,14,2]
# 输出：6
# 解释：在二进制表示中，4 表示为 0100 ，14 表示为 1110 ，2表示为 0010 。（这样表示是为了体现后四位之间关系）
# 所以答案为：
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 
# 2 + 2 = 6
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [4,14,4]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  0 <= nums[i] <= 10⁹ 
#  给定输入的对应答案符合 32-bit 整数范围 
#  
# 
#  Related Topics 位运算 数组 数学 👍 301 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def hammingDistance(self, x, y):
        count = 0
        diff = x ^ y
        while diff:
            if diff & 1:
                count += 1
            diff >>= 1
        return count

    def totalHammingDistance0(self, nums: List[int]) -> int:
        """暴力解法，超时，不通过"""
        total = 0
        n = len(nums)
        for i, num in enumerate(nums):
            for j in range(i + 1, n):
                total += self.hammingDistance(num, nums[j])
        return total

    def totalHammingDistance1(self, nums: List[int]) -> int:
        """按位统计，累计统计每一位上的汉明距离总和。
        对于数组 nums 中的某个元素 val，若其二进制的第 i 位为 1，
        我们只需统计 nums 中有多少元素的第 i 位为 0，即可计算val与其他元素在第 i 位上的汉明距离之和。
        具体地，若长度为 n 的数组 nums 的所有元素二进制的第 i 位共有 c 个 1，n−c 个 0，
        则些元素在二进制的第 i 位上的汉明距离之和为c⋅(n−c)

        每一个数的每一位无非0和1，0和0不会产生距离，1和1也是，
        那只有0和1组合嘛，组合的数量就是0的个数乘以1的个数，那每一位都统计一下就好了。
        """
        distance = 0
        n = len(nums)
        for i in range(30):
            count1 = 0
            for num in nums:
                count1 += (num >> i) & 1
            count0 = n - count1
            distance += count0 * count1
        return distance

    def totalHammingDistance(self, nums: List[int]) -> int:
        """代码简介版"""
        distance = 0
        n = len(nums)
        for i in range(30):
            count1 = sum((num >> i) & 1 for num in nums)
            distance += (n - count1) * count1
        return distance
# leetcode submit region end(Prohibit modification and deletion)
