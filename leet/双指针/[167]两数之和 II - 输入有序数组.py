# 给定一个已按照 升序排列 的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。 
# 
#  函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0]
#  < answer[1] <= numbers.length 。 
# 
#  你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。 
#  
# 
#  示例 1： 
# 
#  
# 输入：numbers = [2,7,11,15], target = 9
# 输出：[1,2]
# 解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
#  
# 
#  示例 2： 
# 
#  
# 输入：numbers = [2,3,4], target = 6
# 输出：[1,3]
#  
# 
#  示例 3： 
# 
#  
# 输入：numbers = [-1,0], target = -1
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= numbers.length <= 3 * 104 
#  -1000 <= numbers[i] <= 1000 
#  numbers 按 递增顺序 排列 
#  -1000 <= target <= 1000 
#  仅存在一个有效答案 
#  
#  Related Topics 数组 双指针 二分查找 
#  👍 506 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """双向奔赴空间复杂度O(1) todo: 可否用二分法加速？"""
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                break
            elif total < target:
                l += 1
            else:
                r -= 1
        return [l + 1, r + 1]

    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        """提前将数字的下标存入字典，空间复杂度O(n)"""
        dic = {num: i for i, num in enumerate(numbers)}
        for i, num in enumerate(numbers):
            diff = target - num
            # if diff in dic and i != dic[diff]:
            # i != dic[diff]不用判断，因为numbers是有序且有唯一解的，所以不会存在[5,3,7]
            if diff in dic:
                return [i + 1, dic[diff] + 1]

    def twoSum11(self, numbers: List[int], target: int) -> List[int]:
        """遍历的同时生成索引字典。
        todo: 这是个bug吧
        测试用例:[3,5,5,7]
        10
        测试结果:[2,3]
        期望结果:[1,4]

        测试用例:[0,0,3,4]
        0
        测试结果:null
        期望结果:[1,2]
        """
        dic = dict()
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in dic and diff != num:
                return [dic[diff] + 1, i + 1]
            else:
                dic[num] = i
# leetcode submit region end(Prohibit modification and deletion)
