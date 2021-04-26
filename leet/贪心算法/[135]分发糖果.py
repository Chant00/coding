# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。 
# 
#  你需要按照以下要求，帮助老师给这些孩子分发糖果： 
# 
#  
#  每个孩子至少分配到 1 个糖果。 
#  评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。 
#  
# 
#  那么这样下来，老师至少需要准备多少颗糖果呢？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[1,0,2]
# 输出：5
# 解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。
#  
# 
#  示例 2： 
# 
#  
# 输入：[1,2,2]
# 输出：4
# 解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这已满足上述两个条件。 
#  Related Topics 贪心算法 
#  👍 539 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """空间O(1)更节省空间，时间复杂度都是O(n)，但是只遍历一遍，比方法一更快"""
        n = len(ratings)
        ret = 1
        inc, dec, pre = 1, 0, 1

        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                dec = 0
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                ret += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                ret += dec
                pre = 1

        return ret

    def candy1(self, ratings: List[int]) -> int:
        """空间O(n)把所有孩子的糖果数初始化为 1；
        先从左往右遍历一遍，如果右边孩子的评分比左边的高，则右边孩子的糖果数更新为左边孩子的 糖果数加 1；
        再从右往左遍历一遍，如果左边孩子的评分比右边的高，且左边孩子当前的糖果数不大于右边孩子的糖果数，则左边孩子的糖果数更新为右边孩子的糖果数加 1。
        通过这两次遍历， 分配的糖果就可以满足题目要求了。这里的贪心策略即为，在每次遍历中，只考虑并更新相邻一 侧的大小关系。"""
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        return sum(candies)
# leetcode submit region end(Prohibit modification and deletion)
