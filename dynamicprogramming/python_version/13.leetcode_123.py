# 题目描述
# hard
# 123. 买卖股票的最佳时机 III
"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

示例 2：
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3：
输入：prices = [7,6,4,3,1] 
输出：0 
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。

示例 4：
输入：prices = [1]
输出：0

提示：
    1 <= prices.length <= 105
    0 <= prices[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

===========================================================================
题解：
    考虑每个时刻i结束后都有四种状态(在当前i时刻结束后所获得的总收益)：
    - dp[i][0] buy1 只买了一次     buy
    - dp[i][1] sell1 买了并卖了一次     buy -> sell
    - dp[i][2] buy2 买了并卖了一次后，又买了一次    buy -> sell -> buy
    - dp[i][3] sell2 完成两次买卖交易    buy -> sell -> buy -> sell
    和上题类似，写出dp转移方程式：

    buy1 = max(buy1, -prices[i])   # 之前就已经买了 or 之前从没完成过交易，当前时刻买了
    sell1 = max(sell1, buy1 + prices[i])   # 之前就完成了一次买卖 or 之前买过一次，当前时刻卖掉
    buy2 = max(buy2, sell1 - prices[i])   # 之前已经第二次买了 or 之前买卖过一次，当前时刻买第二次
    sell2 = max(sell2, buy2 + prices[i])  # 之前完成了两次买卖 or 之前买了第二次，并且当前卖掉第二次

    注意！！！按照dp的话，应该是dp[i] = func(dp[i-1])，而这里用滚动的方法，原位修改了buy1、sell1等值。
    但是这个对于最终的结果不影响，因为更新后的buy1可能只多了一次当天买入，而sell1可以当天卖出，抵消后增益为0。其他同理

    最终返回的是sell2。首先sellx比buyx更合算，因为可以最后一次卖掉，将buyx转化为sellx，且盈利增加。
    另外，sell2比sell1更合算，因为如果sell1最大，那么可以在进行一次当前时刻的buy and sell，转化为sell2，且盈利不变。
    总之，返回sell2。

"""

# 执行用时：236 ms, 在所有 Python 提交中击败了95.80% 的用户
# 内存消耗：21.5 MB, 在所有 Python 提交中击败了61.34% 的用户
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        buy1, buy2 = -prices[0], -prices[0]
        sell1, sell2 = 0, 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2