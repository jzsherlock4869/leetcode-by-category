# 题目如下
# medium
# 739. 每日温度
"""
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

==========================================================================================

本质还是一个next greater number的问题，只是这里输出的不是value，而是对应的index的差，只需要将index压栈，然后在cur和stack.top的比较的时候，
去原来的列表取value即可。
还有一点需要注意：之前的next greater number说明了数组中的数各不相同。这里没有说，需要考虑相等的情况。所以栈应该是一个严格单调递减栈，
因此，入栈条件是cur < stack.top，大于等于都要pop。

结果：
执行用时：332 ms, 在所有 Python 提交中击败了61.47% 的用户
内存消耗：20.7 MB, 在所有 Python 提交中击败了22.22% 的用户
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(temperatures)
        next_hot = [0 for _ in range(n)]
        for i in range(n):
            revi = n - 1 - i
            # 注意这里的while条件：1. 大于等于；2.保存下标，用时现取值
            while stack and temperatures[revi] >= temperatures[stack[-1]]:
                stack.pop(-1)
            if stack:
                next_hot[revi] = stack[-1] - revi
            stack.append(revi)
        return next_hot