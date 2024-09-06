# 给定一个二叉树 root ，返回其最大深度。 
# 
#  二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1,null,2]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数量在 [0, 10⁴] 区间内。 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1865 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """深度优先搜索 时间复杂度：O(n)
        如果我们知道了左子树和右子树的最大深度 l 和 r，那么该二叉树的最大深度即为 max(l,r)+1
        而左子树和右子树的最大深度又可以以同样的方式进行计算。因此我们可以用「深度优先搜索」的方法来计算二叉树的最大深度。
        具体而言，在计算当前二叉树的最大深度时，可以先递归计算出其左子树和右子树的最大深度，
        然后在 O(1) 时间内计算出当前二叉树的最大深度。递归在访问到空节点时退出。
        """
        if root is None:
            return 0
        max_l = self.maxDepth(root.left)
        max_r = self.maxDepth(root.right)
        return max(max_r, max_l) + 1
# leetcode submit region end(Prohibit modification and deletion)
