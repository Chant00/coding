# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。 
# 
#  
# 
#  示例 1： 
# 
#  输入："hello"
# 输出："holle"
#  
# 
#  示例 2： 
# 
#  输入："leetcode"
# 输出："leotcede" 
# 
#  
# 
#  提示： 
# 
#  
#  元音字母不包含字母 "y" 。 
#  
#  Related Topics 双指针 字符串 
#  👍 149 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            if s[l] in vowel and s[r] in vowel:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            else:
                if s[l] not in vowel:
                    l += 1
                if s[r] not in vowel:
                    r -= 1

        return ''.join(s)

    def reverseVowels1(self, s: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            while s[l] not in vowel and l < r:
                l += 1
            while s[r] not in vowel and l < r:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)
# leetcode submit region end(Prohibit modification and deletion)
