# 题目描述
# easy
# 53. 最大子序和
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [0]
输出：0

示例 4：
输入：nums = [-1]
输出：-1

示例 5：
输入：nums = [-100000]
输出：-100000

提示：
    1 <= nums.length <= 3 * 104
    -105 <= nums[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

============================================================
题解：
    由于要求连续性，所以dp[i]应该定义为以nums[i]结尾的最大子序和，于是可以和后面的nums[i+1]建立关系（连续性可以保持）
    递推方法为：
        dp[i] = max(dp[i - 1] + nums[i], nums[i]) (或者写成 = max(dp[i - 1], 0) + nums[i]）
    初始化只需要dp[0] = nums[0]，其他直接递推。

"""

# 执行用时：28 ms, 在所有 Python 提交中击败了56.23% 的用户
# 内存消耗：14.3 MB, 在所有 Python 提交中击败了15.68% 的用户
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], 0) + nums[i]
        return max(dp)


# 省去一个dp数组
# 执行用时：12 ms, 在所有 Python 提交中击败了99.53% 的用户
# 内存消耗：13.9 MB, 在所有 Python 提交中击败了47.90% 的用户
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxi = dpi = nums[0]
        for i in range(1, n):
            dpi = max(dpi, 0) + nums[i]
            if dpi > maxi:
                maxi = dpi
        return maxi
