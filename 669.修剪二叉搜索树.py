#
# @lc app=leetcode.cn id=669 lang=python
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """


        if not root:
            return 
        
        if root.val < L:
            return self.trimBST(root.right ,L , R)
        if root.val > R:
            return self.trimBST(root.left, L, R)

        if root.left:
            if root.left.val < L:
                root.left = root.left.right
                self.trimBST(root, L, R)
            else:
                self.trimBST(root.left, L, R)
        if root.right:
            if root.right.val > R:
                root.right = root.right.left
                self.trimBST(root, L, R)
            else:
                self.trimBST(root.right, L, R)
        return root
        
# @lc code=end

