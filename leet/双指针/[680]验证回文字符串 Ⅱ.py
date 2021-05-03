# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。 
# 
#  示例 1: 
# 
#  
# 输入: "aba"
# 输出: True
#  
# 
#  示例 2: 
# 
#  
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
#  
# 
#  注意: 
# 
#  
#  字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。 
#  
#  Related Topics 字符串 
#  👍 345 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkPalindrome(self, s, l, r):
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # 遇到不等字符，删除左边或删除右边，继续检查子串
                # 不能根据s[l + 1] == s[r]来判断是删除左边还是右边的元素，判断的话需要判断4种情况，非常复杂，运行也不快
                return self.checkPalindrome(s, l + 1, r) or self.checkPalindrome(s, l, r - 1)
        return True

    def validPalindrome1(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        count = 0
        ans = True
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                count += 1
                # 删除左边或右边都能满足，这时就需要两边都尝试一遍
                if s[l + 1] == s[r] and s[r - 1] == s[l] and l + 1 != r:
                    # 删除s[l]
                    l += 1
                    flag1 = True
                    while l < r:
                        if s[l] == s[r]:
                            l += 1
                            r -= 1
                        else:
                            flag1 = False
                            break
                    # 删除s[l]不通过，恢复s[l]，尝试删除s[r]
                    if not flag1:
                        l -= 1
                        r -= 1
                        while l < r:
                            if s[l] == s[r]:
                                l += 1
                                r -= 1
                            else:
                                flag2 = False
                                ans = flag1 or flag2
                                break
                elif s[l + 1] == s[r]:
                    l += 1
                elif s[r - 1] == s[l]:
                    r -= 1
                else:
                    ans = False
                    break
            if count > 1:
                ans = False
                break

        return ans
# leetcode submit region end(Prohibit modification and deletion)
