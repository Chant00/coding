# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
#  
# 
#  
# 
#  提示： 
# 
#  
#  S的长度在[1, 500]之间。 
#  S只包含小写字母 'a' 到 'z' 。 
#  
#  Related Topics 贪心算法 双指针 
#  👍 488 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        tail = {c: i for i, c in enumerate(S)}  # 记录每个字符出现的最后位置
        start, end = 0, 0  # 双指针
        ans = []
        for i, c in enumerate(S):
            end = max(end, tail[c])
            if i == end:
                ans.append(end - start + 1)
                start = end + 1
        return ans

    def partitionLabels1(self, S: str) -> List[int]:
        tail = {c: i for i, c in enumerate(S)}  # 记录每个字符出现的最后位置
        count, max_end = 0, 0  # count直接记录片段的大小
        ans = []
        for i, c in enumerate(S):
            count += 1
            max_end = max(max_end, tail[c])
            if i == max_end:
                ans.append(count)
                count = 0
        return ans
# leetcode submit region end(Prohibit modification and deletion)
