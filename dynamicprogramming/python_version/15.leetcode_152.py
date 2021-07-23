# 题目描述
# medium
# 152. 乘积最大子数组
"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

==================================================================
题解：
    显然，需要分正负讨论，维护一个两列的dp数组，其中dp[i][0]表示nums[i]为结尾的正数积的最大值，dp[i][1]负数绝对值最大值。
    然后，对于nums[i]，考虑其正负，与前面的dp[i-1][x]相乘，将对应的绝对值最大的正数或负数积填充到dp[i][0]和dp[i][1]。
    dp[i][0] = max(dp[i-1][0] * nums[i], nums[i])    if nums[i] > 0
    dp[i][0] = dp[i-1][1] * nums[i]    if nums[i] < 0
    ---
    dp[i][1] = dp[i-1][1] * nums[i]    if nums[i] > 0
    dp[i][1] = min(dp[i-1][0] * nums[i], nums[i])    if nums[i] < 0

    初始化：dp[0][0] = nums[0] if nums[0] > 0 else 0
           dp[0][1] = nums[0] if nums[0] < 0 else 0

    返回值：max{i}(dp[i][0])
"""

# 内存消耗太大，实际上不需要真实开辟dp数组，换滚动数组可以优化。
# 执行用时：28 ms, 在所有 Python 提交中击败了59.87% 的用户
# 内存消耗：15.8 MB, 在所有 Python 提交中击败了5.01% 的用户
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = nums[0] if nums[0] >= 0 else 0
        dp[0][1] = nums[0] if nums[0] < 0 else 0
        for i in range(1, n):
            if nums[i] >= 0:
                dp[i][0] = max(dp[i - 1][0] * nums[i], nums[i])
                dp[i][1] = dp[i - 1][1] * nums[i]
            else:
                dp[i][1] = min(dp[i - 1][0] * nums[i], nums[i])
                dp[i][0] = dp[i - 1][1] * nums[i]
        ret = max([i[0] for i in dp])
        if ret == 0:
            ret = max(nums)
        return ret


# 优化：改成滚动变量，不开辟dp数组，时空复杂度降低。
# 执行用时：24 ms, 在所有 Python 提交中击败了81.35% 的用户
# 内存消耗：13.5 MB, 在所有 Python 提交中击败了73.93% 的用户
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp_pos, dp_neg = 0, 0
        if nums[0] > 0:
            dp_pos = nums[0]
        else:
            dp_neg = nums[0]
        maxi = dp_pos
        for i in range(1, n):
            if nums[i] >= 0:
                dp_pos = max(dp_pos * nums[i], nums[i])
                dp_neg = dp_neg * nums[i]
            else:
                dp_neg_ = min(dp_pos * nums[i], nums[i])
                dp_pos = dp_neg * nums[i]
                dp_neg = dp_neg_
            if dp_pos > maxi:
                maxi = dp_pos
        if maxi == 0:
            maxi = max(nums)
        return maxi