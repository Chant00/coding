# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
#  整数除法仅保留整数部分。
#
#  你可以假设给定的表达式总是有效的。所有中间结果将在 [-2³¹, 2³¹ - 1] 的范围内。
#
#  注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
#
#
#
#  示例 1：
#
#
# 输入：s = "3+2*2"
# 输出：7
#
#
#  示例 2：
#
#
# 输入：s = " 3/2 "
# 输出：1
#
#
#  示例 3：
#
#
# 输入：s = " 3+5 / 2 "
# 输出：5
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 3 * 10⁵
#  s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
#  s 表示一个 有效表达式
#  表达式中的所有整数都是非负整数，且在范围 [0, 2³¹ - 1] 内
#  题目数据保证答案是一个 32-bit 整数
#
#
#  Related Topics 栈 数学 字符串 👍 783 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def calculate1(self, s):
        """
        将所有的计算转为加法，存入栈中，最后求和
        重点是提前初始化一个pre_sign，这样会比较顺畅，
        在非数字的时候去append，同时根据pre_sign计算
        注意i == n - 1时，是最后一个数字，也要走一遍运算
        使用enumerate迭代会更快一点
        执行耗时:92 ms,击败了93.81% 的Python3用户
	    内存消耗:20.4 MB,击败了54.05% 的Python3用户
        """
        n = len(s)
        stack = []
        pre_sign = '+'
        num = 0
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            if i == n - 1 or c in '+-*/':
                if pre_sign == '+':
                    stack.append(num)
                elif pre_sign == '-':
                    stack.append(-num)
                elif pre_sign == '*':
                    stack.append(stack.pop() * num)
                elif pre_sign == '/':
                    stack.append(int(stack.pop() / num))
                # print(stack)
                pre_sign = c
                num = 0

        return sum(stack)

    def calculate2(self, s):
        """
        执行耗时:101 ms,击败了87.11% 的Python3用户
	    内存消耗:20.5 MB,击败了28.17% 的Python3用户
        """
        n = len(s)
        stack = []
        preSign = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                preSign = s[i]
                num = 0
        return sum(stack)

# leetcode submit region end(Prohibit modification and deletion)
