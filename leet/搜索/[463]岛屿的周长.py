# 给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。 
# 
#  网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。 
# 
#  岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿
# 的周长。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# 输出：16
# 解释：它的周长是上面图片中的 16 个黄色的边 
# 
#  示例 2： 
# 
#  
# 输入：grid = [[1]]
# 输出：4
#  
# 
#  示例 3： 
# 
#  
# 输入：grid = [[1,0]]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  row == grid.length 
#  col == grid[i].length 
#  1 <= row, col <= 100 
#  grid[i][j] 为 0 或 1 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 
#  👍 431 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """直接遍历
        官方题解的精髓："对于一个陆地格子的每条边，它被算作岛屿的周长当且仅当这条边为网格的边界或者相邻的另一个格子为水域"。
        我没想到这一点，但是我在纸上画了几个格子，思考了一下陆地格子总数为1，2，3，4的情况，然后发现了一个规律。
        对于单独的格子而言，周长是4，但是当两个格子相邻时，会各自损失1的周长。
        所以问题转化为 找出 岛屿格子 之间的 相邻边。
        """
        nr, nc = len(grid), len(grid[0])
        count = 0
        edge = 0

        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 0:
                    continue
                count += 1
                if i + 1 < nr and grid[i + 1][j] == 1:
                    edge += 1
                if j + 1 < nc and grid[i][j + 1] == 1:
                    edge += 1

        return count * 4 - 2 * edge

    def islandPerimeter1(self, grid: List[List[int]]) -> int:
        """深度优先遍历，可以扩展至，求每个岛屿的周长或最大周长。
        我们可以遍历每个陆地格子，看其四个方向是否为边界或者水域，如果是，将这条边的贡献（即 11）加入答案 \textit{ans}ans 中即可
        已经遍历过的陆地格子，我们设定值为2
        """
        nr, nc = len(grid), len(grid[0])
        perimeter = 0

        def dfs(r, c):
            if not (0 <= r < nr and 0 <= c < nc) or grid[r][c] == 0:
                return 1

            ans = 0
            if grid[r][c] == 1:
                grid[r][c] = 2
                ans += dfs(r + 1, c)
                ans += dfs(r - 1, c)
                ans += dfs(r, c + 1)
                ans += dfs(r, c - 1)

            return ans

        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1:
                    perimeter += dfs(i, j)
        return perimeter
# leetcode submit region end(Prohibit modification and deletion)
