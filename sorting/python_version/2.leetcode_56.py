# 题目描述
# medium
# 56. 合并区间
"""

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

提示：
    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
=========================================

题解：
    首先，按照左端点升序排序，那么可以逐个遍历区间，根据端点决定是否合并。
    维护一个合并后的res = list()
    cur为当前遍历区间，merged为res的最后一个区间，cur的左端点的情况如下两种：
        - cur左端点小于等于merged的右端点，说明重合，用cur和merged的右端点的最大值更新当前merged的右端点。
        - cur左端点大于merged的右端点，说明不重合。将cur加入res中，并将merged = cur，继续遍历。

"""

# 执行用时：24 ms, 在所有 Python 提交中击败了89.20% 的用户
# 内存消耗：14.1 MB, 在所有 Python 提交中击败了93.45% 的用户
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        sort_intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        for interval in sort_intervals:
            if not res:
                res.append(interval)
            # 如果有重叠
            if res[-1][1] >= interval[0]:
                #  由于右端点没排序，所以需要max保证每次都是最大值。
                res[-1][1] = max(res[-1][1], interval[1])
            # 没有重叠，区间加入最终区间
            else:
                res.append(interval)
        return res