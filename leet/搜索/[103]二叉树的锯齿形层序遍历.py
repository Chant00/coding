# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。 
# 
#  例如： 
# 给定二叉树 [3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回锯齿形层序遍历如下： 
# 
#  
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 二叉树 
#  👍 484 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
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
                if cnt % 2 == 1:
                    res.append([i.val for i in reversed(layer2)])
                else:
                    res.append([i.val for i in layer2])
            layer1 = layer2
            layer2 = []
            cnt += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
