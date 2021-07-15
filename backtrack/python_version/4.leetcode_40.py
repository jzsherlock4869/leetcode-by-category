# 题目描述：
# medium
# 40. 组合总和 II
"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
注意：解集不能包含重复的组合。 

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]


提示:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

=====================================================================

题解：
与之前的combination sum问题类似，只是多一个每个元素只能用一次的条件。
该问题的关键在于：candidates列表中的元素可能有重复，但是最终出来的组合结果是要去重的。因此需要backtrack过程中去重。
比如，[1,1,2]，target=3，那么如果直接dfs+（sum >= target和path有序判断剪枝）的话，会得到两个[1,2]。
当重复数量多时，比如[1,1,1,1,1,1,1,1,1,1]，target=15，此时会出现过多重复，全部完成之后剪枝会造成超时。
因此需要backtrack过程中去重。

**** 去重原则：当相同的数字出现在同一层中时，只保留一个，其他的剪枝；（另外还要保持path的有序，避免[1,2]和[2,1]都能得到）

"""

# 执行用时：20 ms, 在所有 Python 提交中击败了97.95% 的用户
# 内存消耗：13.3 MB, 在所有 Python 提交中击败了15.75% 的用户
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = list()
        # 排序很重要，便于检测重复，以及早停（前面大于target，后面更大，就不必进行dfs了）
        candidates = sorted(candidates)
        n = len(candidates)
        # path为路径，summ为path的和（这项也可以不用），idx表示arr = candidates[idx:]
        def backtrack(path, summ, idx):
            if summ == target:
                res.append(path)
                return
            # 为了避免重复，组合类的无顺序的，每个节点只考虑自己右边的部分即可。
            for i in range(idx, n):
                # 关键：同一个层（for循环表示同一层）相同的数，只保留开始的一个
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                new_path = path + [candidates[i]]
                new_idx = i + 1
                new_summ = sum(new_path)
                # 一旦发现大于target的，直接break，后面更大，无需判断。
                if new_summ > target:
                    break
                backtrack(new_path, new_summ, new_idx)
        backtrack([], 0, 0)
        return res

