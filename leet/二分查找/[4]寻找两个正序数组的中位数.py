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
        """划分数组法O(log(min(m,n)))
        将数组分为两部分
            left_part包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]
            right_part包含 nums1[i .. m-1] 和 nums2[j .. n-1]
        奇数：i+j = m-i+n-j+1
        偶数：i+j = m-i+n-j
        j = (m+n+1)//2 - i
            确保m<n，否则j可能是负数
        二分查找[0, m]上（注意不是[0,m)上，因为left_part是到i-1, 不是i），等价与[0,m+1)
            满足max(nums1[i-1], nums2[j-1]) <= min(nums1[i], nums2[j])的最大i
            等价于满足nums1[i-1] <=  nums2[j] 同时 nums[i] > nums2[j-1] 的最大i
            等价于满足nums1[i-1] <=  nums2[j] 的最大i（此时带入i+1，必然有nums[i] > nums2[j-1]）
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        l, r = 0, m + 1  # 注意: 这里是m+1，因为left_part是到i-1, 不是i
        m1, m2 = 0, 0
        while l < r:
            i = l + (r - l) // 2
            j = (m + n + 1) // 2 - i

            nums1_i1 = nums1[i - 1] if i >= 1 else float('-inf')
            nums1_i = nums1[i] if i < m else float('inf')
            nums2_j1 = nums2[j - 1] if j >= 1 else float('-inf')
            nums2_j = nums2[j] if j < n else float('inf')

            if nums1_i1 <= nums2_j:
                m1, m2 = max(nums1_i1, nums2_j1), min(nums1_i, nums2_j)
                l = i + 1
            else:
                r = i

        return m1 if (m + n) % 2 == 1 else (m1 + m2) / 2

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        """划分数组O(log(min(m,n)))
        将数组分为两部分
            前一部分left_part包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]
            后一部分right_part包含 nums1[i .. m-1] 和 nums2[j .. n-1]
        m+n为偶数，left_part的数量应该等于right_part的数量，这时候(max(left)+min(right))/2是中位数。
        m+n为奇数，left_part的数量应该等于right_part的数量+1，这时候max(left)是中位数。
            所以需要变量m1,m2来记录max(left)和min(right)

        m+n为偶数：i+j=m-i+n-j
        m+n为奇数：i+j=m-i+n-j+1
        i+j = (m+n+1)//2 -> j = (m+n+1)//2 - i
        m得小于n，否则j可能是负数，确保num1是size更小的数组。不是就交换一下。
        注意边界条件，i很小时，j可能会超过n。
        nums1[i-1] <= nums2[j]
        nums2[j-1] <= nums1[i]

        对i在[0,m]区间二分搜索，找到满足nums1[i-1] <= nums2[j]的最大的i。（二分查找右边界）
        """
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
            nums_im1 = float('-inf') if i == 0 else nums1[i - 1]  # 当一个数不出现在前一部分时，对应的值为负无穷，就不会对前一部分的最大值产生影响；
            nums_i = float('inf') if i == m else nums1[i]  # 当一个数不出现在后一部分时，对应的值为正无穷，就不会对前一部分的最小值产生影响；
            nums_jm1 = float('-inf') if j == 0 else nums2[j - 1]
            nums_j = float('inf') if j == n else nums2[j]

            # 本来是需要找的是交叉小于，即在[0,m]中的i使得nums_im1 <= nums_j 且 nums_jm1<=nums_i
            # 等价于找到使得nums_im1 <= nums_j的最大的i即可
            if nums_im1 <= nums_j:  # < 或者 <= 都可以
                median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
                # if nums_jm1 <= nums_i:
                #     break
                # 要找的是满足nums_im1 < nums_j的最大的i，所以还要继续l = i + 1，在右边继续查找
                l = i + 1
            else:
                r = i - 1
        return median1 if (m + n) % 2 == 1 else (median1 + median2) / 2

    def getKthElement(self, nums1: List[int], nums2: List[int], k) -> float:
        """O(log(m+n)) 官方题解
        - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
        - 这里的 "/" 表示整除
        - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
        - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
        - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
        - 这样 pivot 本身最大也只能是第 k-1 小的元素
        - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
        - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
        - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数

        注意边界情况， i，j，k三者都有，k==1容易被忽略
        """
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        while True:
            # 边界情况，只需按照i, j = 0, 0的时候考虑就行
            if i == m:
                return nums2[j + k - 1]
            if j == n:
                return nums1[i + k - 1]
            if k == 1:  # 注意：这个容易忘记
                return min(nums1[i], nums2[j])
            # 正常情况
            i_new = min(i + k // 2 - 1, m - 1)  # 防止数组越界
            j_new = min(j + k // 2 - 1, n - 1)
            # nums1[new_i1] == nums2[new_i2]时，当做以下2者中任意情况处理即可，但是不能单独处理为既删除nums1又删除nums2,会死循环
            if nums1[i_new] <= nums2[j_new]:
                # k -= k // 2 # 不能这么写，因为 new_i1 可能取值为m - 1，这时候删除的个数就不是k // 2个，new_i1 - i1 + 1才是绝对正确的
                # 注意: 这里要先更新k再更新i
                k -= i_new - i + 1
                i = i_new + 1
            else:
                k -= j_new - j + 1
                j = j_new + 1

    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        """二分查找"""
        m, n = len(nums1), len(nums2)
        quotient, remainder = divmod(m + n, 2)  # 也可以divmod(m + n + 1, 2)，将奇数和偶数统一，那么后面就不需要quotient + 1
        if remainder == 1:
            return self.getKthElement(nums1, nums2, quotient + 1)  # 注意quotient + 1
        else:
            return (self.getKthElement(nums1, nums2, quotient) + self.getKthElement(nums1, nums2, quotient + 1)) / 2


Solution().findMedianSortedArrays([1, 3], [2])
# leetcode submit region end(Prohibit modification and deletion)
