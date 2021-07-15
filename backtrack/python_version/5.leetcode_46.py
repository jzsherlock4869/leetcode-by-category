# 题目描述
# medium
# 46. 全排列
"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：
输入：nums = [1]
输出：[[1]]

提示：
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    nums 中的所有整数 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

========================================================================
题解：
由于设定了nums数组中数字不相同，所以就是一个简单的dfs回溯的过程。
path每次加一个，arr每次少一个，递归进去作backtrack，不需要剪枝，所有的都保留。
return条件就是arr为空，说明已经把nums中的所有元素都用上了。

"""

# 执行用时：20 ms, 在所有 Python 提交中击败了80.73% 的用户
# 内存消耗：13.2 MB, 在所有 Python 提交中击败了64.52% 的用户
# 这是一个最标准、最简单的backtrack的任务
# 完全按照backtrack的格式写出来如下：
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        def backtrack(path, arr):
            if not arr:
                res.append(path)
                return
            for i, item in enumerate(arr):
                new_path = path + [item]
                new_arr = arr[:i] + arr[i+1:]
                backtrack(new_path, new_arr)
        backtrack([], nums)
        return res