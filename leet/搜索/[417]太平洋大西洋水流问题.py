# 给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。 
# 
#  规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。 
# 
#  请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。 
# 
#  
# 
#  提示： 
# 
#  
#  输出坐标的顺序不重要 
#  m 和 n 都小于150 
#  
# 
#  
# 
#  示例： 
# 
#  
# 
#  
# 给定下面的 5x5 矩阵:
# 
#   太平洋 ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * 大西洋
# 
# 返回:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
#  
# 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 
#  👍 278 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List


class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """用数组表示visited"""
        m, n = len(heights), len(heights[0])
        p_visited = [[False] * n for _ in range(m)]
        a_visited = [[False] * n for _ in range(m)]

        for i in range(m):
            self.dfs(heights, m, n, i, 0, p_visited)
            self.dfs(heights, m, n, i, n - 1, a_visited)
        for j in range(n):
            self.dfs(heights, m, n, 0, j, p_visited)
            self.dfs(heights, m, n, m - 1, j, a_visited)
        ans = []

        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    ans.append([i, j])
        return ans

    def dfs(self, heights, m, n, i, j, visited):
        self.bfs(heights, m, n, i, j, visited)

    def bfs(self, heights, m, n, i, j, visited):
        """队列"""
        queue = deque([[i, j]])
        visited[i][j] = True
        while queue:
            i, j = queue.popleft()
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i_new, j_new = i + x, j + y
                if 0 <= i_new < m and 0 <= j_new < n and not visited[i_new][j_new] \
                        and heights[i_new][j_new] >= heights[i][j]:
                    visited[i_new][j_new] = True
                    queue.append([i_new, j_new])

    def dfs3(self, heights, m, n, i, j, visited):
        """栈"""
        stack = [[i, j]]
        visited[i][j] = True
        while stack:
            i, j = stack.pop()
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i_new, j_new = i + x, j + y
                if 0 <= i_new < m and 0 <= j_new < n and not visited[i_new][j_new] \
                        and heights[i_new][j_new] >= heights[i][j]:
                    visited[i_new][j_new] = True
                    stack.append([i_new, j_new])

    def dfs2(self, heights, m, n, i, j, visited):
        """递归"""
        visited[i][j] = True
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            i_new, j_new = i + x, j + y
            if 0 <= i_new < m and 0 <= j_new < n and not visited[i_new][j_new] \
                    and heights[i_new][j_new] >= heights[i][j]:
                self.dfs2(heights, m, n, i_new, j_new, visited)

    def pacificAtlantic1(self, heights: List[List[int]]) -> List[List[int]]:
        """用set表示visited"""
        m, n = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()

        for i in range(m):
            self.dfs1(heights, m, n, i, 0, p_visited)
            self.dfs1(heights, m, n, i, n - 1, a_visited)
        for j in range(n):
            self.dfs1(heights, m, n, 0, j, p_visited)
            self.dfs1(heights, m, n, m - 1, j, a_visited)

        ans = [list(i) for i in p_visited & a_visited]
        return ans

    def dfs1(self, heights, m, n, i, j, visited):
        """用set表示visited"""
        if (i, j) in visited:
            return

        visited.add((i, j))
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            i_new, j_new = i + x, j + y
            if 0 <= i_new < m and 0 <= j_new < n and (i_new, j_new) not in visited \
                    and heights[i_new][j_new] >= heights[i][j]:
                self.dfs1(heights, m, n, i_new, j_new, visited)
# leetcode submit region end(Prohibit modification and deletion)
