# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
#  Related Topics 数组 回溯 
#  👍 1507 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def permute1(self, nums):
        """"""

        def backtrack(first=0):
            # 所有数都填完了
            if first == n - 1:
                res.append(nums[:])  # 注意nums[:]，拷贝一份，否则最后都是[1,2,3]
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res

    def backtracking(self, nums, level, ans):
        # if level == len(nums) - 1: # 这样写也可以
        if level == len(nums):
            ans.append(nums[:])  # 注意nums[:]，拷贝一份，否则最后都是[1,2,3]
            return
        # for i in range(0, len(nums)): # 不能这么写
        for i in range(level, len(nums)):
            nums[level], nums[i] = nums[i], nums[level]  # 修改当前节点状态
            self.backtracking(nums, level + 1, ans)  # 递归子节点
            nums[level], nums[i] = nums[i], nums[level]  # 回改当前节点状态

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtracking(nums, 0, ans)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
