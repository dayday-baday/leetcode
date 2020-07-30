#
# @lc app=leetcode.cn id=108 lang=python
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 取中点为root点，左边为左子树，右边为右子树
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

# @lc code=end

