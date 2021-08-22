# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
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
#  Related Topics 回溯 
#  👍 285 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalNQueens(self, n: int) -> int:
        """可以直接用[51]的解法，最后返回len(solutions)即可。
        不过因为只要解法数量，所以可以简化很多，记录解法数量就行，不需要生成具体的解法的board
        """

        def backtrack(r):
            if r == n:
                return 1
            else:
                cnt = 0
                for c in range(n):
                    if c in columns or r - c in diagnoal1 or r + c in diagonal2:
                        continue
                    columns.add(c)
                    diagnoal1.add(r - c)
                    diagonal2.add(r + c)
                    cnt += backtrack(r + 1)
                    columns.remove(c)
                    diagnoal1.remove(r - c)
                    diagonal2.remove(r + c)
                return cnt

        columns, diagnoal1, diagonal2 = set(), set(), set()
        return backtrack(0)
# leetcode submit region end(Prohibit modification and deletion)
