# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。 
# 
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，po
# s 仅仅是用于标识环的情况，并不会作为参数传递到函数中。 
# 
#  说明：不允许修改给定的链表。 
# 
#  进阶： 
# 
#  
#  你是否可以使用 O(1) 空间解决此题？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目范围在范围 [0, 104] 内 
#  -105 <= Node.val <= 105 
#  pos 的值为 -1 或者链表中的一个有效索引 
#  
#  Related Topics 链表 双指针 
#  👍 978 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """快慢指针
        对于链表找环路的问题，有一个通用的解法——快慢指针（Floyd 判圈法）。给定两个指针， 分别命名为 slow 和 fast，起始位置在链表的开头。
        每次 fast 前进两步，slow 前进一步。如果 fast 可以走到尽头，那么说明没有环路；
        如果 fast 可以无限走下去，那么说明一定有环路，且一定存 在一个时刻 slow 和 fast 相遇。
        当 slow 和 fast 第一次相遇时，我们将 fast 重新移动到链表开头，
        并 让 slow 和 fast 每次都前进一步。当 slow 和 fast 第二次相遇时，相遇的节点即为环路的开始点。

        数学推导：
        指针走过的长度
            fast: a+n(b+c)+b
            slow: a+b
        由于fast走过的距离为slow的2倍，所以 a+n(b+c)+b = a+b =>a = (n-1)(b+c) + c
        a = (n-1)(b+c) + c
        也就是说，此时再来一个指针从初始位置出发一次只走一步的指针ptr，
        当ptr走过长度a走到入环点时，slow也走过a = (n-1)(b+c) + c 也在入环点。
        """
        slow, fast = head, head
        while True:
            if not (fast and fast.next):
                return
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        fast = head
        while fast != slow:
            slow, fast = slow.next, fast.next
        return fast

    def detectCycle1(self, head):
        """遍历链表中的每个节点，并将它记录下来；一旦遇到了此前遍历过的节点，就可以判定链表中存在环。"""
        seen = set()
        while head:
            if head not in seen:
                seen.add(head)
            else:
                return head
            head = head.next
        return
# leetcode submit region end(Prohibit modification and deletion)
