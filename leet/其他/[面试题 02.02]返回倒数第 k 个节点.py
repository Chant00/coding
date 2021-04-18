# 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。 
# 
#  注意：本题相对原题稍作改动 
# 
#  示例： 
# 
#  输入： 1->2->3->4->5 和 k = 2
# 输出： 4 
# 
#  说明： 
# 
#  给定的 k 保证是有效的。 
#  Related Topics 链表 双指针 
#  👍 66 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        i, j = head, head
        for _ in range(k):
            i = i.next
        while i:
            i = i.next
            j = j.next
        return j.val
# leetcode submit region end(Prohibit modification and deletion)
