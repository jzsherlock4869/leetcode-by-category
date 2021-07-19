# 题目描述
# easy
# 94. 二叉树的中序遍历
"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[2,1]

示例 5：
输入：root = [1,null,2]
输出：[1,2]

提示：
    树中节点数目在范围 [0, 100] 内
    -100 <= Node.val <= 100

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

================================================================
题解：
    递归：注意定义一个函数和一个res，用来保存traversal的路径。
    其实还有两种解法：
        Morris
        迭代
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = list()
        def in_traverse(node):
            if node.left:
                in_traverse(node.left)
            res.append(node.val)
            if node.right:
                in_traverse(node.right)
            return
        in_traverse(root)
        return res