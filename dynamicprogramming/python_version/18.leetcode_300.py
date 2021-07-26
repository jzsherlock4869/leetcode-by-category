# 题目描述
# medium
# 300. 最长递增子序列
"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1

提示：
    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104

进阶：
    你可以设计时间复杂度为 O(n2) 的解决方案吗？
    你能将算法的时间复杂度降低到 O(n log(n)) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

==========================================================================
题解：
    常见动态规划的例题。
    dp[i]表示以nums[i-1]为结尾的LIS，考虑到递增性，只有当后面的数大于nums[i-1]时，才能和当前的这个LIS
    递推关系式：
        - 对于所有j < i，如果nums[j] < nums[i]，说明可以将dp[j]传递到dp[i]上。
          对能够完成传递的，只需要取出最大值+1即可，即：
          dp[i] = max {j<i and nums[j] < nums[i]} dp[j]

"""


# 执行用时：1972 ms, 在所有 Python 提交中击败了66.71% 的用户
# 内存消耗：13.6 MB, 在所有 Python 提交中击败了6.63% 的用户
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
