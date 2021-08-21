# 有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。 
# 
#  我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。 
# 
#  如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。 
# 
#  请返回封闭岛屿的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1
# ,0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。 
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  输入：grid = [[1,1,1,1,1,1,1],
#              [1,0,0,0,0,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,1,0,1,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1]]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length, grid[0].length <= 100 
#  0 <= grid[i][j] <=1 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 
#  👍 84 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """与岛屿数量类似，区别在于，遇到边界的时候岛屿数量不再+1"""
        nr, nc = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r < nr and 0 <= c < nc):
                return False
            if grid[r][c] == 1:
                return True
            grid[r][c] = 1
            b1 = dfs(r, c + 1)
            b2 = dfs(r, c - 1)
            b3 = dfs(r + 1, c)
            b4 = dfs(r - 1, c)
            return all([b1, b2, b3, b4])

        cnt = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 0 and dfs(i, j):
                    cnt += 1
        return cnt
# leetcode submit region end(Prohibit modification and deletion)
