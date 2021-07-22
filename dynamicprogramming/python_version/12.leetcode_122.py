# 题目描述
# easy
# 122. 买卖股票的最佳时机 II
"""
给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

示例 2:
输入: prices = [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3:
输入: prices = [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

提示：
    1 <= prices.length <= 3 * 104
    0 <= prices[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

===============================================================================
题解：
     构造dp矩阵，矩阵大小为 n x 2，dp[i][0] 表示第i天结束后持有股票时的收益；dp[i][1] 表示第i天结束不持有股票的收益。
     注意！这里的持有表示当前买入，或者之前就已经持有。另外，收益指的是当前手里的钱（可以是负数，买入股票相当于负收益）
     于是可以写出递推关系：
          dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])  # 之前持有；之前没有，在i时刻新买入
          dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])  # 之前不持有；之前持有，但是在i时刻卖掉了
     最后返回的结果是：dp[n-1][1]，因为最后肯定是不持有股票更有利于收益。

"""

# 执行用时：36 ms, 在所有 Python 提交中击败了14.15% 的用户
# 内存消耗：17.4 MB, 在所有 Python 提交中击败了5.12% 的用户
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        # 0 不持有；1 持有
        dp[0][1] = - prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]


# 递推只和前面的一个有关，因此不需要真实开辟dp数组，只用滑动数组即可
# 执行用时：24 ms, 在所有 Python 提交中击败了68.04% 的用户
# 内存消耗：13.8 MB, 在所有 Python 提交中击败了60.82% 的用户
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp0, dp1 = 0, - prices[0]
        # 0 不持有；1 持有
        for i in range(1, n):
            dp0_ = max(dp0, dp1 + prices[i])
            dp1_ = max(dp1, dp0 - prices[i])
            dp0, dp1 = dp0_, dp1_
        return dp0