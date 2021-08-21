# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。 
# 
#  一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 
# 0（代表水）包围着。 
# 
#  找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。) 
# 
#  
# 
#  示例 1: 
# 
#  [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#  
# 
#  对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。 
# 
#  示例 2: 
# 
#  [[0,0,0,0,0,0,0,0]] 
# 
#  对于上面这个给定的矩阵, 返回 0。 
# 
#  
# 
#  注意: 给定的矩阵grid 的长度和宽度都不超过 50。 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 
#  👍 535 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    此题是十分标准的搜索题，我们可以拿来练手深度优先搜索。
    一般来说，深度优先搜索类型 的题可以分为主函数和辅函数，
    主函数用于遍历所有的搜索位置，判断是否可以开始搜索，如果 可以即在辅函数进行搜索。
    辅函数则负责深度优先搜索的递归调用。
    当然，我们也可以使用栈 （stack）实现深度优先搜索，但因为栈与递归的调用原理相同，而递归相对便于实现，
    因此刷题时 笔者推荐使用递归式写法，同时也方便进行回溯（见下节）。不过在实际工程上，直接使用栈可 能才是最好的选择，
    一是因为便于理解，二是更不易出现递归栈满的情况。我们先展示使用栈的 写法。
    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """队列，广度优先。 如果改为深度优先，只需要改一个pop(0)改为pop()即可。时间和空间复杂度都是O(R×C)"""
        max_area = 0
        nr, nc = len(grid), len(grid[0])

        def bfs(r, c):
            """放到外面，需要传grid,nr,nc,或者只传grid，然后len(grid), len(grid[0])取nr,nc太麻烦了"""
            ans = 0
            queue = [[r, c]]
            while queue:
                r, c = queue.pop(0)  # 队列，则用pop(0)，先进先出。栈的话，先进后出，用pop。
                if 0 <= r < nr and 0 <= c < nc and grid[r][c] == 1:
                    grid[r][c] = 0
                    ans += 1
                    queue.extend([[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]])
            return ans

        for i in range(nr):
            for j in range(nc):
                max_area = max(max_area, bfs(i, j))
        return max_area

    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        """栈，深度优先。时间和空间复杂度都是O(R×C)"""
        max_area = 0
        nr, nc = len(grid), len(grid[0])

        def dfs(r, c):
            ans = 0
            stack = [[r, c]]
            while stack:
                r, c = stack.pop()  # 栈，先进后出，所以是pop。队列的话，则用pop(0)，先进先出。
                if 0 <= r < nr and 0 <= c < nc and grid[r][c] == 1:
                    grid[r][c] = 0
                    stack.extend([[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]])
                    ans += 1
            return ans

        for i in range(nr):
            for j in range(nc):
                max_area = max(max_area, dfs(i, j))
        return max_area

    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
        """递归，深度优先， 时间和空间复杂度都是O(R×C)，递归的深度最大可能是整个网格的大小，因此最大可能使用O(R×C)的栈空间。"""
        max_area = 0
        nr, nc = len(grid), len(grid[0])

        def dfs(r, c):
            if 0 <= r < nr and 0 <= c < nc and grid[r][c] == 1:
                grid[r][c] = 0
                ans = 1
                ans += dfs(r, c + 1)
                ans += dfs(r, c - 1)
                ans += dfs(r + 1, c)
                ans += dfs(r - 1, c)
                return ans
            else:
                return 0

        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1:  # 这个一行可有可无，如果是求岛屿数量，则必不可少
                    max_area = max(max_area, dfs(i, j))
        return max_area
# leetcode submit region end(Prohibit modification and deletion)
