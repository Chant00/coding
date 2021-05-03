# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
#  
# 
#  示例 2： 
# 
#  输入：c = 3
# 输出：false
#  
# 
#  示例 3： 
# 
#  输入：c = 4
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：c = 2
# 输出：true
#  
# 
#  示例 5： 
# 
#  输入：c = 1
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= c <= 231 - 1 
#  
#  Related Topics 数学 
#  👍 229 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """费马平方和定理
        利用(a - b) ^ 2 + (a + b) ^ 2 = 2 * (a ^ 2 + b ^ 2) = 2 * c先将c一直除以2变为奇数，缩小迭代次数
        再根据费马平方和定理，检查所有模4余3的因子的个数是否为偶数个即可
        """
        if not c:
            return True
        # (a - b) ^ 2 + (a + b) ^ 2 = 2 * (a ^ 2 + b ^ 2) = 2 * c
        while c % 2 == 0:
            c //= 2
        # 费马平方和定理
        if c % 4 == 3:
            return False
        sqrt = int(math.sqrt(c))
        # 每个i都是满足3+4n的数
        for i in range(3, sqrt + 1, 4):
            count = 0
            while c % i == 0:
                c //= i
                count += 1
            if count % 2 != 0:
                return False
        return True

    def judgeSquareSum3(self, c: int) -> bool:
        """费马平方和 官方题解
        费马平方和定理: 奇质数能表示为两个平方数之和的充分必要条件是该质数被 4 除余 1 。
        换个说法: 一个非负整数 c 如果能够表示为两个整数的平方和，当且仅当 c 的所有形如 4k + 3 的质因子的幂均为偶数。
        因此我们需要对 c 进行质因数分解，再判断所有形如 4k + 3 的质因子的幂是否均为偶数(4余3的因子的个数是否为偶数个)即可。
        """
        base = 2
        while base ** 2 < c:
            # 不是因子，枚举下一个
            if c % base != 0:
                base += 1
                continue

            # 计算base的幂
            exp = 0
            while c % base == 0:
                c //= base
                exp += 1

            # 根据 Sum of two squares theorem 验证
            if base % 4 == 3 and exp % 2 != 0:
                return False
            base += 1
        return c % 4 != 3

    def judgeSquareSum2(self, c: int) -> bool:
        """双指针"""
        l, r = 0, int(math.sqrt(c))
        while l <= r:
            if l ** 2 + r ** 2 == c:
                return True
            elif l ** 2 + r ** 2 < c:
                l += 1
            else:
                r -= 1
        return False

    def judgeSquareSum1(self, c: int) -> bool:
        """使用sqrt函数"""
        for i in range(int(math.sqrt(c)) + 1):
            target = c - i ** 2
            tmp = math.sqrt(target)
            if tmp == int(tmp):
                return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
