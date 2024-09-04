# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层序遍历结果： 
# 
#  
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 二叉树 
#  👍 952 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """官方解法，使用队列BFS，BFS改为层序遍历
        https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/bfs-de-shi-yong-chang-jing-zong-jie-ceng-xu-bian-l/
        BFS，第 1 层的结点还没出完，第 2 层的结点就进来了，而且两层的结点在队列中紧挨在一起，我们无法区分队列中的结点来自哪一层
        因此，我们需要稍微修改一下代码，在每一层遍历开始前，
        先记录队列中的结点数量 nn（也就是这一层的结点数量），然后一口气处理完这一层的 nn 个结点。
        """
        res = []
        queue = [root] if root else []

        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            res.append(level)

        return res

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        """我自己的思路"""
        if root is None:
            return []
        res = [[root.val]]
        layer1 = [root]
        layer2 = []
        cnt = 1
        while layer1:
            for i in layer1:
                if i.left is not None:
                    layer2.append(i.left)
                if i.right is not None:
                    layer2.append(i.right)

            if layer2:
                res.append([i.val for i in layer2])
            layer1 = layer2
            layer2 = []
            cnt += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
