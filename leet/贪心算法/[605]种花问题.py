# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。 
# 
#  给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则
# 的情况下种入 n 朵花？能则返回 true ，不能则返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：flowerbed = [1,0,0,0,1], n = 1
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：flowerbed = [1,0,0,0,1], n = 2
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= flowerbed.length <= 2 * 104 
#  flowerbed[i] 为 0 或 1 
#  flowerbed 中不存在相邻的两朵花 
#  0 <= n <= flowerbed.length 
#  
#  Related Topics 贪心算法 数组 
#  👍 344 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """优化：连续0区的规律，可种植花的数量等于(count0 - 1) // 2"""
        # 当前全0区段中连续0的数量，刚开始预设1个0，因为开头花坛的最左边没有花，可以认为存在一个虚无的0
        count, count0 = 0, 1  # count0=1相当于左边补0
        for bed in flowerbed:
            if bed == 0:
                count0 += 1
            else:
                count += (count0 - 1) // 2  # 注意先计算count，再将count0 = 0
                if count > n:
                    return True
                count0 = 0
        # 最后一段0区还未结算：
        count0 += 1  # 相当于右边补0
        count += (count0 - 1) // 2
        return count >= n

    def canPlaceFlowers1(self, flowerbed: List[int], n: int) -> bool:
        """遍历一遍强行种花"""
        count = 0
        # 为了代码流程的统一，可以在数组最左边、数组最右边分别补1个0，意味着花坛左边、右边没有花。
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):  # 注意，flowerbed已经加了两个0，不是最初的长度了
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
            if count >= n:  # 注意这里的缩进，老是写错
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
