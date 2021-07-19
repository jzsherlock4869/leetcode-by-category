# 题目描述
# medium
# 102. 二叉树的层序遍历
"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

返回其层序遍历结果：
[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

=======================================================================
题解：
  层序遍历的典型写法之一：while-condition是que不为空；每一层需要用for循环来限定，即for i in range(len(que))。
  其余直接写即可。

"""

# 执行用时：20 ms, 在所有 Python 提交中击败了75.77% 的用户
# 内存消耗：13.3 MB, 在所有 Python 提交中击败了55.64% 的用户
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        que = [root]
        while que:
            tmp = []
            for i in range(len(que)):
                cur_node = que.pop(0)
                tmp.append(cur_node.val)
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
            res.append(tmp)
        return res