# 题目描述
# easy
# 101. 对称二叉树
"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3

进阶：

你可以运用递归和迭代两种方法解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

============================================================
题解：
    构造一个对比函数，传入两个节点node1和node2，递归判断是否符合要求。
    递归的结构为：node1.left和node2.right（外侧）应该符合；同理，node1.right和node2.left（内侧）应该符合。

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 执行用时：24 ms, 在所有 Python 提交中击败了64.05% 的用户
# 内存消耗：13 MB, 在所有 Python 提交中击败了98.10% 的用户
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_sym(node1, node2):
            # 叶子的左右孩子，两者都到了叶子，返回True
            if not node1 and not node2:
                return True
            # 一个到叶子一个没到，返回False
            if (node1 and not node2) or (node2 and not node1):
                return False
            # 都没到叶子，进行本层比较 + 递归比较
            if not node1.val == node2.val:
                return False
            check_outside = check_sym(node1.left, node2.right)
            check_inside = check_sym(node1.right, node2.left)
            return check_outside and check_inside
        
        return check_sym(root, root)