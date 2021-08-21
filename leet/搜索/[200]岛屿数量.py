# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 
#  👍 1246 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """广度优先搜索"""
        nr, nc = len(grid), len(grid[0])

        def bfs(r, c):
            queue = [[r, c]]
            while queue:
                r, c = queue.pop(0)
                if 0 <= r < nr and 0 <= c < nc and grid[r][c] == '1':
                    grid[r][c] = '0'
                    queue += [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

        count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1
        return count

    def numIslands1(self, grid: List[List[str]]) -> int:
        """深度优先搜索
        主循环:  遍历整个矩阵，当遇到 grid[i][j] == '1' 时，从此点开始做深度优先搜索 dfs，
        岛屿数 count + 1 且在深度优先搜索中删除此岛屿
        dfs: 四个方向深度搜索，将1改为0，即删除岛屿
        """
        nr, nc = len(grid), len(grid[0])

        def dfs(r, c):
            if 0 <= r < nr and 0 <= c < nc and grid[r][c] == '1':
                grid[r][c] = '0'
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':  # 这里这一行必不可少，如果是求最大岛屿面积，这一行则可以去掉
                    dfs(i, j)
                    count += 1
        return count
# leetcode submit region end(Prohibit modification and deletion)
