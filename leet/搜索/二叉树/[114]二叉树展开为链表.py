# 给你二叉树的根结点 root ，请你将它展开为一个单链表： 
# 
#  
#  展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。 
#  展开后的单链表应该与二叉树 先序遍历 顺序相同。 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,5,3,4,null,6]
# 输出：[1,null,2,null,3,null,4,null,5,null,6]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中结点数在范围 [0, 2000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？ 
# 
#  Related Topics 栈 树 深度优先搜索 链表 二叉树 👍 1723 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten1(self, root: Optional[TreeNode]) -> None:
        """递归"""
        arr = []

        def dfs(node):
            if node is None: return
            arr.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        for i in range(1, len(arr)):
            prev, cur = arr[i - 1], arr[i]
            prev.left = None
            prev.right = cur

    def flatten2(self, root: Optional[TreeNode]) -> None:
        """迭代"""
        arr, stack = [], [root]
        while stack:
            node = stack.pop()
            if node is None: return
            arr.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        for i in range(1, len(arr)):
            prev, cur = arr[i - 1], arr[i]
            prev.left = None
            prev.right = cur

    def flatten3(self, root: Optional[TreeNode]) -> None:
        """前序遍历和展开同时进行"""
        if root is None: return
        stack = [root]
        prev = None
        while stack:
            print('stack', stack)
            cur = stack.pop()
            if prev:
                prev.left = None
                prev.right = cur
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            prev = cur

    def flatten(self, root: Optional[TreeNode]) -> None:
        """寻找前驱节点，官方题解方法三，空间复杂度O(1)
        注意到前序遍历访问各节点的顺序是根节点、左子树、右子树。如果一个节点的左子节点为空，则该节点不需要进行展开操作。
        如果一个节点的左子节点不为空，则该节点的左子树中的最后一个节点被访问之后，该节点的右子节点被访问。
        该节点的左子树中最后一个被访问的节点是左子树中的最右边的节点，也是该节点的前驱节点。因此，问题转化成寻找当前节点的前驱节点。

        具体做法是，对于当前节点，如果其左子节点不为空，则在其左子树中找到最右边的节点，作为前驱节点，
        将当前节点的右子节点赋给前驱节点的右子节点，然后将当前节点的左子节点赋给当前节点的右子节点，并将当前节点的左子节点设为空。
        对当前节点处理结束后，继续处理链表中的下一个节点，直到所有节点都处理结束。
        链接：https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solutions/356853/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/
        """
        cur = root
        while cur:
            if cur.left:
                predecessor = cur.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

# leetcode submit region end(Prohibit modification and deletion)
