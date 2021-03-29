#
# @lc app=leetcode.cn id=1470 lang=python
#
# [1470] 重新排列数组
#

# @lc code=start
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(0, n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res

# @lc code=end

