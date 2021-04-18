# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。 
# 
#  说明： 
# 
#  你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？ 
# 
#  示例 1: 
# 
#  输入: [2,2,1]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入: [4,1,2,1,2]
# 输出: 4 
#  Related Topics 位运算 哈希表 
#  👍 1812 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """我们可以利用 x ∧ x = 0 和 x ∧ 0 = x 的特点，将数组内所有的数字进行按位异或。
        出现两次 的所有数字按位异或的结果是 0，0 与出现一次的数字异或可以得到这个数字本身。"""
        ans = 0
        for i in nums:
            ans ^= i
        return ans
# leetcode submit region end(Prohibit modification and deletion)
