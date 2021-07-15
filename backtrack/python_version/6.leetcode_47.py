# 题目描述
# medium
# 47. 全排列 II
"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

提示：
    1 <= nums.length <= 8
    -10 <= nums[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

===============================================================
题解：
    和不重复的全排列一样的思路，但是为了考虑取消重复，需要在同一层的节点进行剪枝
    当我们说“同一层级”的时候，我们实际上在说“for 循环内”

"""


# 执行用时：16 ms, 在所有 Python 提交中击败了99.75% 的用户
# 内存消耗：13.3 MB, 在所有 Python 提交中击败了82.78% 的用户
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        n = len(nums)
        # 通过相邻判断去重的话，必须先排序
        nums.sort()
        def backtrack(path, arr):
            if not arr:
                res.append(path)
                return
            last = None
            for i, item in enumerate(arr):
                # 对相邻的两个的重复性判断，如果重复了，只保留一个
                if item == last:
                    continue
                # 其他操作与不重复的情况相同
                new_path = path + [item]
                new_arr = arr[:i] + arr[i+1:]
                backtrack(new_path, new_arr)
                last = item
        backtrack([], nums)
        return res
