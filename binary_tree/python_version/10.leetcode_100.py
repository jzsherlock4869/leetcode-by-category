# 题目描述
# easy
# 100. 相同的树
"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1：
输入：p = [1,2,3], q = [1,2,3]
输出：true

示例 2：
输入：p = [1,2], q = [1,null,2]
输出：false

示例 3：
输入：p = [1,2,1], q = [1,1,2]
输出：false

提示：
    两棵树上的节点数目都在范围 [0, 100] 内
    -104 <= Node.val <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

===============================================================
题解：
    本题简单，只需要递归判断本节点val相等，并且本节点为root的子树符合sameTree（递归调用）

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 执行用时：12 ms, 在所有 Python 提交中击败了94.76% 的用户
# 内存消耗：12.9 MB, 在所有 Python 提交中击败了94.87% 的用户
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 都到了叶子的左右孩子
        if not p and not q:
            return True
        # 一个到了叶子，而另一个却没到
        if (not p and q) or (not q and p):
            return False
        # 两个都没到叶子节点，比较当前、左子树、右子树三个结果
        if not p.val == q.val:
            return False
        check_left = self.isSameTree(p.left, q.left)
        check_right = self.isSameTree(p.right, q.right)
        return check_left and check_right