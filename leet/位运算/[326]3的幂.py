# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。 
# 
#  整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 27
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 0
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 9
# 输出：true
#  
# 
#  示例 4： 
# 
#  
# 输入：n = 45
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  -231 <= n <= 231 - 1 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你能不使用循环或者递归来完成本题吗？ 
#  
#  Related Topics 数学 
#  👍 157 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """log3MaxInt=2**32/2-1
        3^{log3MaxInt}=3^{19.56}=3^{19}=1162261467
        因此，我们应该返回 true 的 n 的可能值是 3^0, 3^13, … 3^{19}。
        因为3是质数，所以3^{19}的除数只有 3^0，3^1, … 3^{19}，因此我们只需要将 3^{19}除以 n。
        若余数为 0 意味着 n 是 3^{19}的除数，因此是 3 的幂
        """
        return n > 0 and 1162261467 % n == 0
# leetcode submit region end(Prohibit modification and deletion)
