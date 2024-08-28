# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。 
# 
#  注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: num1 = "2", num2 = "3"
# 输出: "6" 
# 
#  示例 2: 
# 
#  
# 输入: num1 = "123", num2 = "456"
# 输出: "56088" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num1.length, num2.length <= 200 
#  num1 和 num2 只能由数字组成。 
#  num1 和 num2 都不包含任何前导零，除了数字0本身。 
#  
# 
#  Related Topics 数学 字符串 模拟 👍 1365 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = [0] * (m + n) # 结果最多为 m + n 位数
        for i in range(m - 1, -1, -1):
            n1 = ord(num1[i]) - ord('0')
            for j in range(n - 1, -1, -1):
                n2 = ord(num2[j]) - ord('0')
                p = res[i + j + 1] + n1 * n2  # 注意这里res[i + j + 1]容易漏
                p1, p2 = divmod(p, 10)
                res[i + j] += p1
                res[i + j + 1] = p2
        i = 0
        # 注意这里m + n - 1，这样不用return s if len(s) else "0"
        # 保留了最后一位数字，结果为0的时候能正常输出"0"
        while i < m + n - 1 and res[i] == 0:
            i += 1
        s = ""
        for j in range(i, m + n):
            s += str(res[j])
        # return s if len(s) else "0"
        return s
        # i = 0
        # s = ""
        # flag = True
        # while i < m + n:
        #     if not (res[i] == 0 and flag):
        #         s += str(res[i])
        #         flag = False
        #     if i == m + n - 2:
        #         flag = False
        #     i += 1
        # # return s if len(s) else "0"  # 注意边界条件
        # return s


# print(Solution().multiply("123", "456"))
# print(123 * 456)
print(Solution().multiply("0", "0"))
# print(Solution().multiply("2", "3"))
# leetcode submit region end(Prohibit modification and deletion)
