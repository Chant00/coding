# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。 
# 
#  对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i
# ]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。 
#  
# 
#  示例 1: 
# 
#  
# 输入: g = [1,2,3], s = [1,1]
# 输出: 1
# 解释: 
# 你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
# 虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
# 所以你应该输出1。
#  
# 
#  示例 2: 
# 
#  
# 输入: g = [1,2], s = [1,2,3]
# 输出: 2
# 解释: 
# 你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
# 你拥有的饼干数量和尺寸都足以让所有孩子满足。
# 所以你应该输出2.
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= g.length <= 3 * 104 
#  0 <= s.length <= 3 * 104 
#  1 <= g[i], s[j] <= 231 - 1 
#  
#  Related Topics 贪心算法 
#  👍 321 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """排序+贪心
        因为饥饿度最小的孩子最容易吃饱，所以我们先考虑这个孩子。为了尽量使得剩下的饼干可 以满足饥饿度更大的孩子，
        所以我们应该把大于等于这个孩子饥饿度的、且大小最小的饼干给这 个孩子。
        满足了这个孩子之后，我们采取同样的策略，考虑剩下孩子里饥饿度最小的孩子，直到 没有满足条件的饼干存在。
        """
        g.sort()
        s.sort()
        child, cookie = 0, 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child
# leetcode submit region end(Prohibit modification and deletion)
