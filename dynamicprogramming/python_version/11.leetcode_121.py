# 题目描述
# easy
# 121. 买卖股票的最佳时机
"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

提示：
    1 <= prices.length <= 105
    0 <= prices[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

===========================================================================
题解：
    方案 1：
    假设我们要在i时刻卖出股票，那么买入的价格为min(prices[...i]])时所赚的差值是最多的（注意：这里固定了卖出时刻）
    最后在所有卖出时刻中取最大值即可。
    如果写成公式的话，则：best_earn = max {i} (prices[i] - min {j <= i} (prices[j]))

"""

# 方案 1
# 执行用时：100 ms, 在所有 Python 提交中击败了97.67% 的用户
# 内存消耗：19.9 MB, 在所有 Python 提交中击败了34.63% 的用户
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_mini = prices[0]
        best_earn = 0
        n = len(prices)
        for i in range(1, n):
            # 遍历到的位置表示：在当前时刻 卖出 股票， prices[i] - buy_mini 为此时的最大收益
            # 每次遍历更新最小值（当前时间i之前（含）的最小值）
            if prices[i] < buy_mini:
                buy_mini = prices[i]
            # 更新最大收益
            if prices[i] - buy_mini > best_earn:
                best_earn = prices[i] - buy_mini
        return best_earn