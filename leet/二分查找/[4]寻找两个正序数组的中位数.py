# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#  
# 
#  示例 3： 
# 
#  
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
#  
# 
#  示例 4： 
# 
#  
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
#  
# 
#  示例 5： 
# 
#  
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -106 <= nums1[i], nums2[i] <= 106 
#  
# 
#  
# 
#  进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？ 
#  Related Topics 数组 二分查找 分治算法 
#  👍 4045 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """划分数组"""
        m, n = len(nums1), len(nums2)
        if m > n:  # 确保m<n，否则计算j = (m + n + 1) // 2 - i可能会出现负数
            return self.findMedianSortedArrays(nums2, nums1)

        l, r = 0, m
        median1, median2 = 0, 0  # median1前一部分的最大值,median2后一部分的最小值
        while l <= r:
            i = l + (r - l) // 2
            j = (m + n + 1) // 2 - i
            # i=0、i=m、j=0、j=n 的临界条件处理
            # nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            nums_im1 = float('-inf') if i == 0 else nums1[i - 1]
            nums_i = float('inf') if i == m else nums1[i]
            nums_jm1 = float('-inf') if j == 0 else nums2[j - 1]
            nums_j = float('inf') if j == n else nums2[j]

            if nums_im1 < nums_j:
                median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
                # 找的是满足nums_im1 < nums_j的最大的i，所以还要继续l = i + 1，在右边继续查找
                l = i + 1
            else:
                r = i - 1
        return median1 if (m + n) % 2 == 1 else (median1 + median2) / 2

    def getKthElement(self, nums1, nums2, k):
        """
        - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
        - 这里的 "/" 表示整除
        - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
        - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
        - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
        - 这样 pivot 本身最大也只能是第 k-1 小的元素
        - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
        - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
        - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
        """
        m, n = len(nums1), len(nums2)
        i1, i2 = 0, 0
        while True:
            # 特殊情况，只需按照i1, i2 = 0, 0的时候考虑就行
            if i1 == m:
                return nums2[i2 + k - 1]
            if i2 == n:
                return nums1[i1 + k - 1]
            if k == 1:
                return min(nums1[i1], nums2[i2])
            # 正常情况
            new_i1 = min(i1 + k // 2 - 1, m - 1)  # 防止数组越界
            new_i2 = min(i2 + k // 2 - 1, n - 1)
            # nums1[new_i1] == nums2[new_i2]时，当做以下2者中任意情况处理即可，但是不能单独处理为既删除nums1又删除nums2,会死循环
            if nums1[new_i1] < nums2[new_i2]:  # < 或者<=都可以
                # k -= k // 2 # 不能这么写，因为 new_i1 可能取值为m - 1，这时候删除的个数就不是k // 2个，new_i1 - i1 + 1才是绝对正确的
                k -= new_i1 - i1 + 1
                i1 = new_i1 + 1
            else:
                k -= new_i2 - i2 + 1
                i2 = new_i2 + 1

    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        """二分查找"""
        m, n = len(nums1), len(nums2)
        quotient, remainder = divmod(m + n, 2)  # 也可以divmod(m + n + 1, 2)，将奇数和偶数统一，那么后面就不需要quotient + 1
        if remainder == 1:
            return self.getKthElement(nums1, nums2, quotient + 1)  # 注意quotient + 1
        else:
            return (self.getKthElement(nums1, nums2, quotient) + self.getKthElement(nums1, nums2, quotient + 1)) / 2
# leetcode submit region end(Prohibit modification and deletion)
