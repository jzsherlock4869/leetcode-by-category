# 题目描述
# easy
# 112. 路径总和
"""
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，
判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
叶子节点 是指没有子节点的节点。

示例 1：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true

示例 2：
输入：root = [1,2,3], targetSum = 5
输出：false

示例 3：
输入：root = [1,2], targetSum = 0
输出：false

提示：
    树中节点的数目在范围 [0, 5000] 内
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

==========================================================
题解：
    方案 1： 递归求解，按顺序返回。
    方案 2： BFS，记录每层的结果，在叶子节点处check当前的sum是否满足target

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 执行用时：52 ms, 在所有 Python 提交中击败了5.09% 的用户
# 内存消耗：16.5 MB, 在所有 Python 提交中击败了81.77% 的用户
# TODO: 时间开销大, 原因待查
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node, target):
            if not node:
                return False
            if not node.left and not node.right:
                if target == node.val:
                    return True
                else:
                    return False
            ck_left = dfs(node.left, target - node.val)
            ck_right = dfs(node.right, target - node.val)
            return ck_left or ck_right
        return dfs(root, targetSum)

