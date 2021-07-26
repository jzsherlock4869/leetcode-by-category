# 题目描述
# medium
# 198. 打家劫舍
"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

提示：
    1 <= nums.length <= 100
    0 <= nums[i] <= 400

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

===================================================================================
题解：
     构造dp数组，其中dp[i]表示前(i+1)个房屋里能取到的最大值，递推关系可以分类讨论写出：
     - 如果取了nums[i]，那么不能取nums[i-1]，此时总数最大为 dp[i-2] + nums[i]
     - 如果没有取nums[i]，那么可以取nums[i-1]，此时总数最大为 dp[i-1]
     注意！dp[i-1]如果包含了不取nums[i]的情况，那么它就变成了dp[i-2]，肯定比dp[i-2] + nums[i]更小。所以不影响结果。

     初始化：dp[0]，前1个，只能是 dp[0] = nums[0]
     dp[1]，前两个，dp[1] = max(nums[0], nums[1])

     剩下的项递推即可。

"""

# 执行用时：16 ms, 在所有 Python 提交中击败了79.36% 的用户
# 内存消耗：12.8 MB, 在所有 Python 提交中击败了92.41% 的用户
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]
