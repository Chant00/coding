# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。 
# 
#  你可以按 任何顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
# 
#  示例 2： 
# 
#  
# 输入：n = 1, k = 1
# 输出：[[1]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
#  Related Topics 数组 回溯 
#  👍 669 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def backtrack(self, n, k, comb, ans, pos):
        if len(comb) == k:
            ans.append(comb[:])
            return
        # for i in range(1, n + 1):  # 这样写的话，会重复一遍，比如[1,4]和[4,1]这种重复
        for i in range(pos, n + 1):  # 从1开始到n，所以注意是n+1
            comb.append(i)
            self.backtrack(n, k, comb, ans, i + 1)
            comb.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        comb = []
        self.backtrack(n, k, comb, ans, 1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
