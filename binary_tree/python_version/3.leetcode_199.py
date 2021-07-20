# 题目描述
# medium
# 199. 二叉树的右视图
"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1:
输入: [1,2,3,null,5,null,4]
输出: [1,3,4]

示例 2:
输入: [1,null,3]
输出: [1,3]

示例 3:
输入: []
输出: []

提示:
    二叉树的节点个数的范围是 [0,100]
    -100 <= Node.val <= 100 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

===================================================================================
题解：
    1. 最易于理解的方法：层序遍历 + 分层返回 + 每层取最后一个组成res
    2. DFS，将depth传参进去，每次记录该depth下的第一个元素（通过比较depth和当前res的长度即可知道是否是第一个达到该depth）

"""


# DFS 解法：代码简洁，需要理解 depth == len(res) 这个if condition
# 执行用时：12 ms, 在所有 Python 提交中击败了97.66% 的用户
# 内存消耗：13.1 MB, 在所有 Python 提交中击败了28.83% 的用户

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        depth = 0
        res = list()
        def dfs(node, d):
            if d == len(res):
                res.append(node.val)
            if node.right:
                dfs(node.right, d+1)
            if node.left:
                dfs(node.left, d+1)
            return
        dfs(root, depth)
        return res


# 层序遍历（分层输出）取最右值
# 执行用时：16 ms, 在所有 Python 提交中击败了93.15% 的用户
# 内存消耗：13 MB, 在所有 Python 提交中击败了55.32% 的用户

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = list()
        que = [root]
        while que:
            temp = []
            for i in range(len(que)):
                node = que.pop(0)
                # 注意！append是原位操作！！！存储的是node.val不是node！！！
                temp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(temp)
        rightview = [item[-1] for item in res]

        return rightview
            
