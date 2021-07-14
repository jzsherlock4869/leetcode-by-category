# 题目如下：
# hard
# 42. 接雨水
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

示例 2：

输入：height = [4,2,0,3,2,5]
输出：9

 
提示：

    n == height.length
    0 <= n <= 3 * 104
    0 <= height[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

====================================================================

解法：
这个题目的关键点在于：如何判断一个位置（也就是数组中的某个元素所表示的柱子）能承接的雨水量？答案是：它取决于该位置两侧的最小值与它本身的差。
如果两侧的值至少有一个比它小，那么说明它是全局最大值，不会有雨水。如果两遍都比它大，那么，说明这个位置在一个洼地里面，于是有雨水，水量就是
min(left_max, right_max) - cur_height

方法1，直接计算。
根据上面的分析，一个最直接的方法就是对每个点，找它左边最大值和右边最大值，然后遍历计算即可。

方法2，单调栈。
维护一个单调递减栈，从左往右依次填充雨水。如果遇到cur > stack.top，那么说明又有新的积水。
于是计算这一段的水量。height = min(stack_next_greater, cur), width = pos[cur] - pos[stack_next_greater] - 1
stack pop后，继续计算。这个方法每次只计算一“层”，当stack.pop全部完成后，每次算的雨水（矩形）就叠起来了。

方法3，双指针法。
记录在在双指针部分吧。

"""

# 直接解决：
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0
        left_max_list = []
        right_max_list = []
        cur_left_max, cur_right_max = height[0], height[-1]
        for i in range(n):
            if height[i] > cur_left_max:
                cur_left_max = height[i]
            left_max_list.append(cur_left_max)
        for j in range(n):
            i = n - 1 - j
            if height[i] > cur_right_max:
                cur_right_max = height[i]
            right_max_list = [cur_right_max] + right_max_list 
        rain_list = [max(min(left_max_list[i], right_max_list[i]) - height[i], 0) \
                        for i in range(n)]
        return sum(rain_list)


# 单调栈法：
