# 题目描述
# medium
# 236. 二叉树的最近公共祖先
"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”


示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：
输入：root = [1,2], p = 1, q = 2
输出：1

提示：
    树中节点数目在范围 [2, 105] 内。
    -109 <= Node.val <= 109
    所有 Node.val 互不相同 。
    p != q
    p 和 q 均存在于给定的二叉树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

====================================================================
题解：
    如果用返回null来表示在该节点为根的树中没有p或者q的话，那么可以设立如下规则：
    - 如果当前node为空，即叶子节点的left和right，那么返回null
    - 如果当前node等于p或者q，那么返回当前node
    上面是边界条件，用于直接返回。下面考虑，如果对中间的一个节点，有了左右两子树的返回值，汇总逻辑如何？
    - 如果左边右边都为null，说明该node下面的树中间没有p和q，LCA不在此处，所以直接返回null
    - 如果左边为null，右边不为null，说明LCA在右边，直接返回right的结果即可；反之亦然
    - 如果两边都不是null，说明p和q在左右两边各有一个，于是自己就是LCA，返回当前node

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 执行用时：44 ms, 在所有 Python 提交中击败了98.24% 的用户
# 内存消耗：24.8 MB, 在所有 Python 提交中击败了61.25% 的用户
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        # 先做相等的判断非常重要，如果相等直接返回，可以保证p为q的祖先时，返回的是p而不是q。
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return None
        if not left:
            return right
        if not right:
            return left
        return root