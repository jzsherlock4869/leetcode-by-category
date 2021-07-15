# 题目描述
# medium
# 78. 子集
"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

提示：
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    nums 中的所有元素 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

======================================================================
题解：
    子集，实际上就是对于每个数，进行 取 或 不取 的选择。
    因此，对于backtrack，子节点就是两个，一个为取，一个不取。
    由于是组合，不考虑顺序，需要注意去重（按照index，只做从左往右的递归）

"""

# 执行用时：20 ms, 在所有 Python 提交中击败了61.04% 的用户
# 内存消耗：13.2 MB, 在所有 Python 提交中击败了66.44%
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        # 标准的backtrack
        def backtrack(path, arr):
            if not arr:
                res.append(path)
                return
            new_path = path + [arr[0]]
            # 如果不取当前的节点arr[0]
            backtrack(path, arr[1:])
            # 如果取了当前节点arr[0]
            backtrack(new_path, arr[1:])
        backtrack([], nums)
        return res

