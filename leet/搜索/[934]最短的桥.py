# 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。） 
# 
#  现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。 
# 
#  返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。） 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：A = [[0,1],[1,0]]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：A = [[0,1,0],[0,0,0],[0,0,1]]
# 输出：2
#  
# 
#  示例 3： 
# 
#  
# 输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# 输出：1 
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length == A[0].length <= 100 
#  A[i][j] == 0 或 A[i][j] == 1 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 
#  👍 179 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        1.通过DFS查找第一个岛，作为多源广度搜索的source，并且标记为已访问，并且标记为0
        2.基于source进行BFS多源广度搜索
        """
        m, n = len(grid), len(grid[0])
        source = deque()

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] == 0:
                return
            grid[r][c] = 0
            source.append((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        find = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not find:  # not find 只找一个岛
                    dfs(i, j)
                    find = True

        # 找到一个岛后，宽度优先，层序遍历，遇到第二个岛则停止迭代，此时层数即为最短桥距离
        seen = set(source)
        d = 0
        # 不能这么写，因为一开始的 (r, c) 必然in seen，而我们要判断的是(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)是否in seen
        # while source:
        #     for _ in range(len(source)):  # 这里的循环是层序遍历的方法，每一层的时候距离d+=1
        #         r, c = source.popleft()
        #         if not (0 <= r < m and 0 <= c < n) or (r, c) in seen:
        #             continue
        #
        #         if grid[r][c] == 1:
        #             return d
        #         else:
        #             seen.add((r, c))
        #             source.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])
        #     d += 1

        while source:
            for _ in range(len(source)):  # 这里的循环是层序遍历的方法，每一层的时候距离d+=1
                i, j = source.popleft()
                for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if not (0 <= r < m and 0 <= c < n) or (r, c) in seen:
                        continue
                    if grid[r][c] == 0:
                        source.append((r, c))
                        seen.add((r, c))
                    else:
                        return d
            d += 1

        return d
# leetcode submit region end(Prohibit modification and deletion)
