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
    def mySqrt0(self, x: int) -> int:
        """袖珍计算器算法，用指数函数 exp  和对数函数 ln  代替平方根函数的方法
        x^0.5 = (e^ln(x))^0.5 = e^(0.5*ln(x))"""
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        # 浮点数问题，我们应当找出 ans  与 ans1  中哪一个是真正的答案
        return ans + 1 if (ans + 1) ** 2 <= x else ans

    def mySqrt(self, x: int) -> int:
        """牛顿法
        这里先把x改名为n，方便写函数推导，写代码的时候再反过来。
        定义函数 f(x) = x**2 - n
        一阶泰勒展开，并令其=0求驻点 f(x0) + f'(x0)(x-x0) = 0
        x = x0-f(x0)/f'(x0) = x0-(x0**2-n)/2x0 = x0- (x0-n/x0)/2
        """
        if x == 0:  # 注意这个特殊条件，否则后续n - (n - x / n) / 2会除以0。
            return 0
        threshold = 0.0001
        n = x
        while True:
            pre = n
            n = n - (n - x / n) / 2
            # 这里比检查abs(mid ** 2 - x) <= threshold更好，一个是不用再计算平方，
            # 一个是可能出现死循环，threshold=1e-7，x=2147395599时，46339.999989210184会一直死循环，只能是调小阈值
            if abs(n - pre) < threshold:
                break
        return int(n)

    def mySqrt3_1(self, x: int) -> int:
        """牛顿法"""
        if x == 0:
            return 0
        threshold = 0.0001
        n = x
        pre = n
        n = n - (n - x / n) / 2
        while abs(n - pre) > threshold:
            pre = n
            n = n - (n - x / n) / 2
        return int(n)

    def mySqrt4(self, x: int) -> int:
        """牛顿法
        判断条件abs(n ** 2 - x) > threshold，计算平方，不如mySqrt3
        f(x) = x**2 - n
        f(x0) + f'(x0)(x-x0) = 0
        x = x0-f(x0)/f'(x0)
          = x0- (x0-n/x0)/2
        """
        threshold = 0.001
        n = x
        while abs(n ** 2 - x) > threshold:
            n = n - (n - x / n) / 2
        return int(n)

    def mySqrt1(self, x: int) -> int:
        """二分法1
        在[0, x)上 找到满足t**2=x的t
        由于这里限制t是整数，所以是找到满足t**2<=x的最大t，即t的右边界
        注意：搜索区间[0, x)存在特殊情况，x=0和1的时候 ，区间为空
        """
        # 后面使用的是while l < r在[0, x)上搜索，所以x=0和1的时候，搜索区间为空，要特殊处理
        if x <= 1:
            return x
        l, r = 0, x
        while l < r:
            mid = l + (r - l) // 2
            if mid ** 2 <= x:
                l = mid + 1
            elif mid ** 2 > x:
                r = mid
        return l - 1

    def mySqrt2(self, x: int) -> int:
        """二分法2，优于二分法1
        在[0, x)上 找到满足t**2=x的t
        由于这里限制t是整数，所以是找到满足t**2<=x的最大t，即t的右边界
        注意：搜索区间[0, x)存在特殊情况，x=0和1的时候 ，区间为空
        所以改为 在[0, x]上 找到满足t**2<=x的最大t，即t的右边界
        """
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid ** 2 <= x:
                l = mid + 1
            elif mid ** 2 > x:
                r = mid - 1
        return l - 1
# leetcode submit region end(Prohibit modification and deletion)
