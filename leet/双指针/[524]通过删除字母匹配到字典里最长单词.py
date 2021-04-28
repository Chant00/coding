# 给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符
# 串。如果答案不存在，则返回空字符串。 
# 
#  示例 1: 
# 
#  
# 输入:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 
# 输出: 
# "apple"
#  
# 
#  示例 2: 
# 
#  
# 输入:
# s = "abpcplea", d = ["a","b","c"]
# 
# 输出: 
# "a"
#  
# 
#  说明: 
# 
#  
#  所有输入的字符串只包含小写字母。 
#  字典的大小不会超过 1000。 
#  所有输入的字符串长度不会超过 1000。 
#  
#  Related Topics 排序 双指针 
#  👍 144 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findLongestWord2(self, s: str, dictionary: List[str]) -> str:
        """不排序，迭代过程中更新最长单词"""
        max_word = ''
        for word in dictionary:
            i = j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            # j走到尽头，说明匹配
            if j == len(word):
                if len(word) > len(max_word) or (len(word) == len(max_word) and word < max_word):
                    max_word = word
        return max_word

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        """先排序，再双指针迭代匹配 这个算法复杂度不不排序更高，但是实际却更快，因为如果先找到最长的那个匹配单词，能省去一些不必要的匹配过程"""
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            i = j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            # j走到尽头，说明匹配
            if j == len(word):
                return word
        return ''

# leetcode submit region end(Prohibit modification and deletion)
