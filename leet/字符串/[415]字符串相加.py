# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。 
# 
#  你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：num1 = "11", num2 = "123"
# 输出："134"
#  
# 
#  示例 2： 
# 
#  
# 输入：num1 = "456", num2 = "77"
# 输出："533"
#  
# 
#  示例 3： 
# 
#  
# 输入：num1 = "0", num2 = "0"
# 输出："0"
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num1.length, num2.length <= 10⁴ 
#  num1 和num2 都只包含数字 0-9 
#  num1 和num2 都不包含任何前导零 
#  
# 
#  Related Topics 数学 字符串 模拟 👍 848 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = ''
        i, j, carry = m - 1, n - 1, 0
        # carry记录加法时相前进位的值
        while i >= 0 or j >= 0 or carry != 0:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            s = n1 + n2 + carry
            carry, s2 = divmod(s, 10)
            res = str(s2) + res
            i -= 1
            j -= 1
        return res


print(Solution().addStrings("11", "123"))
# leetcode submit region end(Prohibit modification and deletion)
