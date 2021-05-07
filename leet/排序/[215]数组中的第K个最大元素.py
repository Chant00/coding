# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  示例 1: 
# 
#  输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4 
# 
#  说明: 
# 
#  你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。 
#  Related Topics 堆 分治算法 
#  👍 1058 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import random
from typing import List


class Solution:
    def findKth(self, nums, k, low, high):
        rand = random.randint(low, high)
        nums[rand], nums[low] = nums[low], nums[rand]

        l, r = low, high
        base = nums[low]
        while l < r:
            while l < r and nums[r] < base:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] >= base:
                l += 1
            nums[r] = nums[l]
        nums[l] = base
        if l == k - 1:
            return l
        elif l < k - 1:
            return self.findKth(nums, k, l + 1, high)
        else:
            return self.findKth(nums, k, low, l - 1)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """基于快排O(n)"""
        i = self.findKth(nums, k, 0, len(nums) - 1)
        return nums[i]

    def sift_down(self, nums, start, end):
        parent, child = start, 2 * start + 1
        while child < end:
            if child + 1 < end and nums[child + 1] > nums[child]:
                child += 1
            if nums[parent] < nums[child]:
                nums[parent], nums[child] = nums[child], nums[parent]
                parent = child
                child = 2 * parent + 1
            else:
                break

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """基于堆排O(n*log(n))"""
        for start in range((len(nums) - 2) // 2, -1, -1):
            self.sift_down(nums, start, len(nums))
        # 执行k-1次删除操作，则第K大的数字此时正好在堆顶
        for end in range(len(nums) - 1, len(nums) - k, -1):
            nums[0], nums[end] = nums[end], nums[0]
            self.sift_down(nums, 0, end)
        return nums[0]
# leetcode submit region end(Prohibit modification and deletion)
