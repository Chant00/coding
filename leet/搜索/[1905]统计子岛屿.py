# 给你两个 m x n 的二进制矩阵 grid1 和 grid2 ，它们只包含 0 （表示水域）和 1 （表示陆地）。一个 岛屿 是由 四个方向 （水平或者竖
# 直）上相邻的 1 组成的区域。任何矩阵以外的区域都视为水域。 
# 
#  如果 grid2 的一个岛屿，被 grid1 的一个岛屿 完全 包含，也就是说 grid2 中该岛屿的每一个格子都被 grid1 中同一个岛屿完全包含，那
# 么我们称 grid2 中的这个岛屿为 子岛屿 。 
# 
#  请你返回 grid2 中 子岛屿 的 数目 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], gri
# d2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# 输出：3
# 解释：如上图所示，左边为 grid1 ，右边为 grid2 。
# grid2 中标红的 1 区域是子岛屿，总共有 3 个子岛屿。
#  
# 
#  示例 2： 
# 
#  输入：grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], gri
# d2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# 输出：2 
# 解释：如上图所示，左边为 grid1 ，右边为 grid2 。
# grid2 中标红的 1 区域是子岛屿，总共有 2 个子岛屿。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid1.length == grid2.length 
#  n == grid1[i].length == grid2[i].length 
#  1 <= m, n <= 500 
#  grid1[i][j] 和 grid2[i][j] 都要么是 0 要么是 1 。 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 
#  👍 22 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import deque


class Solution:
    """与岛屿数量类似，多一步检验，grid1[i][j]是否也为1"""

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """广度优先 队列"""
        nr, nc = len(grid1), len(grid1[0])

        def dfs(r, c):
            # queue = [[r, c]]
            queue = deque([[r, c]])
            flag = True
            while queue:
                # r, c = queue.pop(0) # 使用pop(0)会非常耗时，所以最好是用真正的队列deque 双边队列，可以左右pop和append
                r, c = queue.popleft()
                if 0 <= r < nr and 0 <= c < nc and grid2[r][c] == 1:
                    grid2[r][c] = 0
                    if grid1[r][c] != 1:
                        flag = False
                    queue.extend([[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]])
            return flag

        cnt = 0
        for i in range(nr):
            for j in range(nc):
                if grid2[i][j] == 1:
                    cnt += int(dfs(i, j))
        return cnt

    def countSubIslands2(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """深度优先 栈"""
        nr, nc = len(grid1), len(grid1[0])

        def dfs(r, c):
            stack = [[r, c]]
            flag = True
            while stack:
                r, c = stack.pop()
                if 0 <= r < nr and 0 <= c < nc and grid2[r][c] == 1:
                    grid2[r][c] = 0
                    if grid1[r][c] != 1:
                        flag = False
                    stack.extend([[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]])
            return flag

        cnt = 0
        for i in range(nr):
            for j in range(nc):
                if grid2[i][j] == 1:
                    cnt += int(dfs(i, j))
        return cnt

    def countSubIslands1(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """递归"""
        nr, nc = len(grid1), len(grid1[0])

        def dfs(r, c):
            # 注意这两个条件，这样反过来写，更好写
            if not (0 <= r < nr and 0 <= c < nc and grid2[r][c] == 1):
                return True
            if grid1[r][c] != 1:
                return False
            grid2[r][c] = 0
            b1 = dfs(r, c + 1)
            b2 = dfs(r, c - 1)
            b3 = dfs(r - 1, c)
            b4 = dfs(r + 1, c)

            return all([b1, b2, b3, b4])

        cnt = 0
        for i in range(nr):
            for j in range(nc):
                if grid2[i][j] == 1:
                    cnt += int(dfs(i, j))
        return cnt
# leetcode submit region end(Prohibit modification and deletion)
