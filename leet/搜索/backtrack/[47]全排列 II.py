# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
#  Related Topics 数组 回溯 
#  👍 777 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def backtrack(self, nums, idx, perm, visited, ans):
        # if idx == len(nums) - 1:
        if idx == len(nums):
            ans.append(perm[:])  # 注意perm[:]拷贝
            return

        # for i in range(idx, len(nums)):
        for i in range(0, len(nums)):
            # i > 0 and nums[i] == nums[i - 1] and not visited[i - 1] 保证不会重复
            if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                continue
            perm.append(nums[i])
            visited[i] = True
            self.backtrack(nums, idx + 1, perm, visited, ans)
            visited[i] = False
            perm.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """解决重复问题，先排序，保证在填第idx个数的时候重复数字只会被填入一次即可"""
        nums.sort()
        visited = [False] * len(nums)
        perm = []
        ans = []
        self.backtrack(nums, 0, perm, visited, ans)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
