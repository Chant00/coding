# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -105 <= nums[i] <= 105 
#  
#  Related Topics 数组 双指针 
#  👍 3350 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b for循环的双指针
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ret = []
        for i in range(n):
            if nums[i] > 0:  # 若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果
                return ret
            if i > 0 and nums[i] == nums[i - 1]:  # 重复元素跳过
                continue
            l, r = i + 1, n - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    ret.append([nums[i], nums[l], nums[r]])
                    # 找到一组后还要继续找，并不是只有唯一解
                    while l < r and nums[l] == nums[l + 1]:  # 重复元素跳过
                        l += 1
                    # 右边的重复元素其实不用跳过也行，因为左边那个唯一符合的值跳过了，就不会有符合l了，也不会有重复的添加到ans里了
                    # while l < r and nums[r] == nums[r - 1]:  # 重复元素跳过
                    #     r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return ret
# leetcode submit region end(Prohibit modification and deletion)
