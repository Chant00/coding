# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "AB
# CCED"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SE
# E"
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "AB
# CB"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n = board[i].length 
#  1 <= m, n <= 6 
#  1 <= word.length <= 15 
#  board 和 word 仅由大小写英文字母组成 
#  
# 
#  
# 
#  进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？ 
#  Related Topics 数组 回溯 矩阵 
#  👍 996 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def dfs1(self, board, m, n, word, i, j, k):
        """栈"""
        ans = False
        stack = [[i, j]]
        while stack:
            tmp = stack.pop()
            if tmp[0] is None:
                # None做标记，是退出回溯的时候，这里存放了ijt用于恢复数据
                k -= 1
                i, j, t = tmp[1]
                board[i][j] = t
            else:
                i, j = tmp
                if (0 <= i < m and 0 <= j < n) and k < len(word) and word[k] == board[i][j]:
                    if k == len(word) - 1:
                        return True

                    # 在进回溯时把字符改成‘0’，出回溯再改回去，就不用额外存储是否访问了
                    t = board[i][j]
                    board[i][j] = '0'
                    k += 1
                    # 这里要注意的点，是递归中出回溯比较好些，这里则需要在栈中多加入一个标记
                    # [None, (i, j, t)]，None做标记，说明此时是退出回溯的时候，这里存放了ijt,用于之后推出回溯时恢复数据
                    stack.extend([[None, (i, j, t)], [i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]])

        return ans

    def dfs(self, board, m, n, word, i, j, k):
        """递归"""
        if k == len(word):
            return True
        if not (0 <= i < m and 0 <= j < n) or word[k] != board[i][j]:
            return False
        # 在进回溯时把字符改成‘0’，出回溯再改回去，就不用额外存储是否访问了
        t = board[i][j]
        board[i][j] = '0'
        b1 = self.dfs(board, m, n, word, i + 1, j, k + 1)
        b2 = self.dfs(board, m, n, word, i - 1, j, k + 1)
        b3 = self.dfs(board, m, n, word, i, j + 1, k + 1)
        b4 = self.dfs(board, m, n, word, i, j - 1, k + 1)
        board[i][j] = t
        return any([b1, b2, b3, b4])

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, m, n, word, i, j, 0):
                        return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
