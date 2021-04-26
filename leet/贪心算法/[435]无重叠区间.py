# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。 
# 
#  注意: 
# 
#  
#  可以认为区间的终点总是大于它的起点。 
#  区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。 
#  
# 
#  示例 1: 
# 
#  
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
# 
# 输出: 1
# 
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
#  
# 
#  示例 2: 
# 
#  
# 输入: [ [1,2], [1,2], [1,2] ]
# 
# 输出: 2
# 
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
#  
# 
#  示例 3: 
# 
#  
# 输入: [ [1,2], [2,3] ]
# 
# 输出: 0
# 
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
#  
#  Related Topics 贪心算法 
#  👍 408 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """在选择要保留区间时，区间的结尾十分重要：
        选择的区间结尾越小，余留给其它区间的空间就越大，就越能保留更多的区间。
        因此，我们采取的贪心策略为，优先保留结尾小且不相交的区间。
        具体实现方法为，先把区间按照结尾的大小进行增序排序，
        每次选择结尾最小且和前一个选择的区间不重叠的区间。
        """
        intervals.sort(key=lambda x: x[1])
        ans = 0
        tail = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < tail:
                ans += 1
            else:
                tail = intervals[i][1]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
