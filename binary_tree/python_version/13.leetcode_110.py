# 题目描述
# easy
# 110. 平衡二叉树
"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：true

示例 2：
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false

示例 3：
输入：root = []
输出：true

提示：
    树中的节点数在范围 [0, 5000] 内
    -104 <= Node.val <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

==========================================================
题解：
    模板题，balance的充要条件：左子树和右子树相差不超过1；左子树balance（递归）；右子树balance（递归）
    方法 1：直接定义一个depth，然后递归调用balance函数，用depth计算每个node为root的子树的深度（可以看到，复杂度较高）
    方法 2：自底向上，如果平衡，返回高度，否则返回-1。这样就可以少调用depth函数。

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 执行用时：52 ms, 在所有 Python 提交中击败了39.31% 的用户
# 内存消耗：18.2 MB, 在所有 Python 提交中击败了40.98% 的用户
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1
        if not root:
            return True
        if not abs(depth(root.left) - depth(root.right)) <= 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)