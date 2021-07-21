# 题目描述
# easy
# 111. 二叉树的最小深度
"""
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：2

示例 2：
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5

提示：
    树中节点数的范围在 [0, 105] 内
    -1000 <= Node.val <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

===================================================================
题解：
    递归求解。需要注意的一点是，和最大深度不同，不能直接用min(left, right) + 1的方式，
    因为如果左右子树其中有一个为空，那么这样返回的是1，但是没有到叶子节点，不能算最小深度，应该去非空的那一边去寻找
    于是得到最小深度的逻辑：
        - 如果left为空，则本层深度为min_depth(right) + 1；反之亦然
        - 如果left和right都为空（叶子），本层深度为1 (可以直接包含在上一规则中，只需要设定min_depth(None) = 0)
        - 如果left和right都不为空，本层深度min(min_depth(left), min_depth(right)) + 1

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 执行用时：628 ms, 在所有 Python 提交中击败了96.36% 的用户
# 内存消耗：92.8 MB, 在所有 Python 提交中击败了33.64% 的用户
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # 如果缺少了左或右子树，那么min depth由另一边决定
        if not root.left and root.right:
            return self.minDepth(root.right) + 1
        if not root.right and root.left:
            return self.minDepth(root.left) + 1
        # 如果左右子树都没有，说明是叶子，直接返回 1
        if not root.left and not root.right:
            return 1
        # 左右子树都有的时候，和max_depth一样
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

