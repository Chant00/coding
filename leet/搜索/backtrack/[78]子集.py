# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  nums 中的所有元素 互不相同 
#  
#  Related Topics 位运算 数组 回溯 
#  👍 1288 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def backtrack(self, nums, sub, ans, pos):
        """与[77]组合的区别，只在于，是否判断len(comb) == k"""
        ans.append(sub[:])
        for i in range(pos, len(nums)):
            sub.append(nums[i])
            # print(sub)
            self.backtrack(nums, sub, ans, i + 1)
            sub.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        self.backtrack(nums, sub, ans, 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().subsets([1, 2, 3]))
