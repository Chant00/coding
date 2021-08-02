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
