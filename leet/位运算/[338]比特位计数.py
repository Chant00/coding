# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。 
# 
#  示例 1: 
# 
#  输入: 2
# 输出: [0,1,1] 
# 
#  示例 2: 
# 
#  输入: 5
# 输出: [0,1,1,2,1,2] 
# 
#  进阶: 
# 
#  
#  给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？ 
#  要求算法的空间复杂度为O(n)。 
#  你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。 
#  
#  Related Topics 位运算 动态规划 
#  👍 711 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """动态规划+位运算"""

    def countBits(self, num: int) -> List[int]:
        dp = [0]
        for i in range(1, num + 1):
            dp.append(dp[i >> 1] + (i & 1))  # 不断右移一位，检查最后一位是否为1
        return dp

    def countBits3(self, num: int) -> List[int]:
        dp = [0]
        for i in range(1, num + 1):
            dp.append(dp[i & (i - 1)] + 1)  # i & (i - 1)将i的二进制中最后一个1给整没了，所以+1刚好
        return dp

    def countBits2(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(num + 1):
            dp[i] = dp[i - 1] + 1 if i & 1 else dp[i >> 1]  # 奇数则dp[i]=d[i-1],偶数则dp[i]=dp[i >> 1]
        return dp
# leetcode submit region end(Prohibit modification and deletion)
