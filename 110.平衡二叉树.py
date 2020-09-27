#
# @lc app=leetcode.cn id=110 lang=python
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.flag = True

        def helper(node):
            # 比较左右两子树的深度，并返回自己的深度
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            if abs(left - right) > 1:
                self.flag = False
            return max(left, right) + 1
        helper(root)
        return self.flag
# @lc code=end

