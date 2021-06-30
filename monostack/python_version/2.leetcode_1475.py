# 题目如下：
# easy
# 1475. 商品折扣后的最终价格
"""
给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。
商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，
其中 j 是满足 j > i 且 prices[j] <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。
请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。
 

示例 1：

输入：prices = [8,4,6,2,3]
输出：[4,2,4,2,3]
解释：
商品 0 的价格为 price[0]=8 ，你将得到 prices[1]=4 的折扣，所以最终价格为 8 - 4 = 4 。
商品 1 的价格为 price[1]=4 ，你将得到 prices[3]=2 的折扣，所以最终价格为 4 - 2 = 2 。
商品 2 的价格为 price[2]=6 ，你将得到 prices[3]=2 的折扣，所以最终价格为 6 - 2 = 4 。
商品 3 和 4 都没有折扣。

示例 2：

输入：prices = [1,2,3,4,5]
输出：[1,2,3,4,5]
解释：在这个例子中，所有商品都没有折扣。

示例 3：

输入：prices = [10,1,1,6]
输出：[9,0,1,6]
 

提示：

    1 <= prices.length <= 500
    1 <= prices[i] <= 10^3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

==================================================================================================

解法：题意很明确，就是一个求解数组的每个元素的next smaller元素的问题。和next greater思路完全一样，考虑单调栈。
但是由于找的是最小值，所以需要单调递增栈。

对于这一点（什么时候递减、什么时候递增），我们可以这样考虑：既然要找最接近的更小的数，那么，我们希望如果符合条件的话，越近越好。
而如果离得近的不符合，那么我们只能退而求其次，向更远（更往后）的地方去找。那么，自然地，近处要留下的数大，远处的小。因为如果远处的数x比近处的y还大，
那么，如果x满足要求（小于cur），那么y必定也满足，而且y更近，应该选y，所以x没有任何用处。所以可以直接丢掉x，也就是丢掉离得远还大的数，
即栈顶比cur大的时候要pop。这样得到的必然是个递增栈。

结果：
执行用时：32 ms, 在所有 Python 提交中击败了63.75% 的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了28.75% 的用户
"""

class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        next_smaller_list = [0 for i in range(len(prices))] # 这里的默认值为0了，存的是value不是id，因此不影响。
        for i in range(len(prices)):
            revi = len(prices) - 1 - i
            while stack and prices[revi] < stack[-1]:
                stack.pop(-1)
            # 只能在栈不空的时候更新next smaller
            if stack:
                next_smaller_list[revi] = stack[-1]
            # 不要忘了压栈
            stack.append(prices[revi])

        res = []
        for i in range(len(prices)):
            res.append(prices[i] - next_smaller_list[i])
        return res
