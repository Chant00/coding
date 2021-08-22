# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。 
# 
#  
#  
#  每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[["Q"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。 
#  
#  
#  
#  Related Topics 数组 回溯 
#  👍 980 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """官方题解，时间复杂度：O(N!) 空间复杂度：O(N)
        遍历行，所以行自然就不同了
        1. 不同列，columns 一个set，记录遍历过的列
        2. 不同左上->右下斜线，diagnoal1记录遍历过的斜线元素，规律: r-c相同
        3. 不同右上->左下斜线，diagnoal2记录遍历过的斜线元素，规律: r+c相同
        """

        def gen_board():
            board = []
            for i in range(n):
                row[queens[i]] = 'Q'
                board.append(''.join(row))
                row[queens[i]] = '.'
            return board

        def backtrack(r):
            if r == n:
                board = gen_board()
                solutions.append(board)
            else:
                for c in range(n):
                    if c in columns or r - c in diagnoal1 or r + c in diagonal2:
                        continue
                    queens[r] = c
                    columns.add(c)
                    diagnoal1.add(r - c)
                    diagonal2.add(r + c)
                    backtrack(r + 1)
                    columns.remove(c)
                    diagnoal1.remove(r - c)
                    diagonal2.remove(r + c)

        solutions = []
        queens = [-1] * n
        columns, diagnoal1, diagonal2 = set(), set(), set()
        row = ['.'] * n
        backtrack(0)
        return solutions

# leetcode submit region end(Prohibit modification and deletion)
