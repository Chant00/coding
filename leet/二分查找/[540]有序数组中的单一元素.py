# 给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。 
# 
#  示例 1: 
# 
#  
# 输入: [1,1,2,3,3,4,4,8,8]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,3,7,7,10,11,11]
# 输出: 10
#  
# 
#  注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。 
#  Related Topics 二分查找 
#  👍 232 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """O(log(n/2))只需要对偶数索引进行二分查找"""
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if mid % 2 == 1:
                mid -= 1  # 我们需要确保 mid 是偶数，如果为奇数，则将其减1。同时确保右边是偶数个元素
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]

    def singleNonDuplicate1(self, nums: List[int]) -> int:
        """二分法O(log(n)) 和136题相似，但是136是无需数组，只能遍历O(n)"""
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == nums[mid + 1]:
                if (mid - l) % 2 == 1:
                    r = mid - 1
                else:
                    l = mid + 2
            elif nums[mid] == nums[mid - 1]:
                if (r - mid) % 2 == 0:
                    r = mid - 2
                else:
                    l = mid + 1
            else:
                return nums[mid]
        return nums[l]
# leetcode submit region end(Prohibit modification and deletion)
