# 题目描述
# medium
# 39. 组合总和
"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
    所有数字（包括 target）都是正整数。
    解集不能包含重复的组合。 

示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例 2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


提示：
    1 <= candidates.length <= 30
    1 <= candidates[i] <= 200
    candidate 中的每个元素都是独一无二的。
    1 <= target <= 500

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

=========================================================================

题解：
注意到时每个数字次数无限制，因此，arr在backtrack过程中不变。target用来约束path的合法性。
另外，考虑到组合的无序性，需要在path延伸的时候做一个控制，保证有序。
如解法1。严格按照template的顺序，但是速度较低。

解法2进行优化，首先，排序后的candidates数组中，如果前面一个已经大于target，后面的所有都不用再考察了，直接break
速度有了提升。
"""


# 解法 1 
# 执行用时：96 ms, 在所有 Python 提交中击败了24.64% 的用户
# 内存消耗：13 MB, 在所有 Python 提交中击败了80.24% 的用户
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = list()
        def backtrack(path, arr):
            # 退出机制，合法path判断
            if sum(path) >= target:
                if sum(path) == target:
                    res.append(path)
                return
            # arr不变，因为可以无限次用
            for item in arr:
                # 保证path的有序性，避免重复
                if path:
                    if item < path[-1]:
                        continue
                new_path = path + [item]
                backtrack(new_path, arr)
        backtrack([], candidates)
        return res



# 解法 2
# 执行用时：36 ms, 在所有 Python 提交中击败了88.73% 的用户
# 内存消耗：13.3 MB, 在所有 Python 提交中击败了11.56% 的用户
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = list()
        def backtrack(path, arr):
            if sum(path) == target:
                res.append(path)
                return
            for item in arr:
                if path:
                    if item < path[-1]:
                        continue
                path = path + [item]
                # 注意，将大于target的判断移动到了这里
                # 并且用了break，这是sorted的结果。
                if sum(path) > target:
                    break
                backtrack(path, arr)
                path = path[:-1]
        backtrack([], candidates)
        return res

