# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链
# 表节点，返回 反转后的链表 。
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目为 n 
#  1 <= n <= 500 
#  -500 <= Node.val <= 500 
#  1 <= left <= right <= n 
#  
# 
#  
# 
#  进阶： 你可以使用一趟扫描完成反转吗？ 
#  Related Topics 链表 
#  👍 904 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """头插法，注意穿针引线的顺序
        curr：指向待反转区域的第一个节点 left；一直在向后移动
        next：永远指向 curr 的下一个节点，循环过程中，curr 变化以后 next 会变化；
        pre：永远指向待反转区域的第一个节点 left 的前一个节点，在循环过程中不变。
        """
        dummy_node = ListNode(-1, head)  # 设置 dummyNode 是这一类问题的一般做法
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next

        for _ in range(right - left):
            next = cur.next
            cur.next = next.next  # 1. cur指向next.next
            next.next = pre.next  # 2. next指向pre.next
            pre.next = next  # 3. pre指向next
        return dummy_node.next
# leetcode submit region end(Prohibit modification and deletion)
