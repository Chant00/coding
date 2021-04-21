# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。 
# 
#  说明： 
# 
#  
#  拆分时可以重复使用字典中的单词。 
#  你可以假设字典中没有重复的单词。 
#  
# 
#  示例 1： 
# 
#  输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
#  
# 
#  示例 2： 
# 
#  输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
#  
# 
#  示例 3： 
# 
#  输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#  
#  Related Topics 动态规划 
#  👍 948 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        """dp[i] 表示 s 的前 i 位是否可以用 wordDict 中的单词表示。
        初始化 dp[0]=True，空字符可以被表示。
        """
        n = len(s)
        dp = [True] + [False] * n
        wordDict = set(wordDict)
        for i in range(n):
            for j in range(i + 1, n + 1):
                # 若 dp[i]=True 说明s[:i]是符合的，加上s[i:j] in wordDict，那么s[:j]都是符合的
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        1. 为什么dp要初始化为n + 1的大小, dp[i]表示[i - k, i)是否匹配?
        因为如果从0开始, dp[i]表示[i - k + 1, i]匹配, 则无法初始化dp的首项, 导致第一个单词需要特判
        2. 为什么是dp[i] = dp[i] or dp[i - sz] ?
        只要命中词典中的一个单词就为True，遍历wordDict时，其中某一次命中wordDict，就说明s[:i]符合了
        """
        n = len(s)
        dp = [True] + [False] * n
        for i in range(1, n + 1):
            for word in wordDict:
                word_size = len(word)
                if i >= word_size and s[i - word_size:i] == word:
                    dp[i] = dp[i] or dp[i - word_size]
                    # 可以替换为
                    # if dp[i - word_size]:
                    #     dp[i] = True
        return dp[n]
# leetcode submit region end(Prohibit modification and deletion)
