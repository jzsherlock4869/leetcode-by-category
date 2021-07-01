# 题目如下：
# medium
# 503. 下一个更大元素 II
"""
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，
这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

注意: 输入数组的长度不会超过 10000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

=====================================================================

解法：
仍然是next greater number，只不过这里的数组变成了循环数组。处理方式其实很简单，只需要将数组复制一份和原数组拼起来，
就可以让循环数组中的元素“看到”前面的元素了。
需要注意：遍历过程需要从后往前，进行2n次，但是真正有效的只有前面的n个数。
（原则上来讲，如果将循环数组真正展开，应该是无限次延拓，后半部分结果不真实）
另外，这“复制+拼接”只是逻辑上的，编程的时候不需要再开辟一个数组，只需要用mod运算即可。

"""

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(nums)
        next_gr_list = [-1 for _ in range(n)]
        # 因为只有两次，这里直接循环了两次，第一次是后面的n元素的数组，只压栈不输出
        # 第二次在第一次的栈的基础上，和普通的next greater一样，压栈并输出结果。这种写法避免了mod的判断。
        # 因为是从后往前入栈，因此对下标进行mod容易出错，所以采用了直接做两遍的策略。
        for loop in range(2):
            for i in range(n):
                revi = n - 1 - i
                while stack and stack[-1] <= nums[revi]:
                    stack.pop(-1)
                if loop == 1 and stack:
                    next_gr_list[revi] = stack[-1]
                stack.append(nums[revi])
        return next_gr_list


