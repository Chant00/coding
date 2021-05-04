# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。 
# 
#  示例 1: 
# 
#  
# 输入:
# "tree"
# 
# 输出:
# "eert"
# 
# 解释:
# 'e'出现两次，'r'和't'都只出现一次。
# 因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
#  
# 
#  示例 2: 
# 
#  
# 输入:
# "cccaaa"
# 
# 输出:
# "cccaaa"
# 
# 解释:
# 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
# 注意"cacaca"是不正确的，因为相同的字母必须放在一起。
#  
# 
#  示例 3: 
# 
#  
# 输入:
# "Aabb"
# 
# 输出:
# "bbAa"
# 
# 解释:
# 此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
# 注意'A'和'a'被认为是两种不同的字符。
#  
#  Related Topics 堆 哈希表 
#  👍 242 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def frequencySort(self, s: str) -> str:
        """桶排序"""
        freq = dict()
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        bucket_size = (len(s) + 1)
        bucket = [[] for _ in range(bucket_size)]  # 不能写成[[]]*bucket_size
        # bucket[i]存放频数为i的字符
        for k, v in freq.items():
            bucket[v].append(k)
        # 倒序遍历bucket，连接字符，注意ch * i
        res = ''
        for i in range(bucket_size - 1, 0, -1):
            if bucket[i]:
                for ch in bucket[i]:
                    res += ch * i
        return res
# leetcode submit region end(Prohibit modification and deletion)
