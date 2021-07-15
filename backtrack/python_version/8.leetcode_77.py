# 题目描述
# medium
# 77. 组合
"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

===========================================================
题解：用k作为return，注意去重。

"""


# 执行用时：364 ms, 在所有 Python 提交中击败了71.69% 的用户
# 内存消耗：17.2 MB, 在所有 Python 提交中击败了80.68% 的用户
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = list()
        # path表示已经选中的，idx表示当前的根节点
        # 叶子结点只需要从idx的右边取即可
        def backtrack(path, idx):
            if len(path) == k:
                res.append(path)
                return
            for i in range(idx, n + 1):
                # 当前idx加入path，并把idx右边移动一位（表示idx已被取走）
                new_path = path + [i]
                new_idx = i + 1
                backtrack(new_path, new_idx)
        backtrack([], 1)
        return res
