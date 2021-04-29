# 实现 int sqrt(int x) 函数。 
# 
#  计算并返回 x 的平方根，其中 x 是非负整数。 
# 
#  由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。 
# 
#  示例 1: 
# 
#  输入: 4
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
#      由于返回类型是整数，小数部分将被舍去。
#  
#  Related Topics 数学 二分查找 
#  👍 667 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        """袖珍计算器算法，用指数函数 exp  和对数函数 ln  代替平方根函数的方法
        x^0.5 = (e^ln(x))^0.5 = e^(0.5*ln(x))"""
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans

    def mySqrt3(self, x: int) -> int:
        """牛顿法"""
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            # 这里比检查abs(mid ** 2 - x) <= threshold更好，一个是不用再计算平方，
            # 一个是可能出现死循环，threshold=1e-7，x=2147395599时，46339.999989210184会一直死循环，只能是调小阈值
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)

    def mySqrt2(self, x: int) -> int:
        """二分法，直接取整数"""
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def mySqrt1(self, x: int) -> int:
        """二分法，最终取int，中间判断0和1"""
        threshold = 0.001
        l, r = 0, x
        ans = 0
        while l <= r:
            mid = (l + r) / 2
            if abs(mid ** 2 - x) <= threshold:
                if 0 < mid < 1:
                    ans = 1
                else:
                    ans = int(mid)
                break
            elif mid ** 2 > x:
                r = mid
            else:
                l = mid
        return ans
# leetcode submit region end(Prohibit modification and deletion)
