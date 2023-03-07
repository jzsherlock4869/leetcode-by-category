# 一些常用的 binary tree 相关的常用模板
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 前序、中序、后序遍历（递归方法）：
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(node, cur_list):
            if node is None:
                return cur_list
            left_list = helper(node.left, cur_list)
            right_list = helper(node.right, cur_list)
            # return [node.val] + left_list + right_list
            return left_list + [node.val] + right_list
            # return left_list + right_list + [node.val]

        traverse_list = list()
        traverse_list = helper(root, traverse_list)

        return traverse_list



# 前序、中序、后序遍历（迭代方法）：




# 层序遍历（不需要分层返回）模板：
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        traverse_out = list()
        node_queue = [root]
        while len(node_queue) > 0:    
            node = node_queue.pop(0)
            traverse_out.append(node.val)
            if node.left is not None:
                node_queue.append(node.left)
            if node.right is not None:
                node_queue.append(node.right)
        return traverse_out


# 层序遍历（需要分层返回）模板：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        traverse_out = list()
        node_queue = [root]
        while len(node_queue) > 0:
            cur_layer = list()
            for i in range(len(node_queue)):
                node = node_queue.pop(0)
                cur_layer.append(node.val)
                if node.left is not None:
                    node_queue.append(node.left)
                if node.right is not None:
                    node_queue.append(node.right)
            traverse_out.append(cur_layer)
        return traverse_out

# 求解树的深度（最大深度）
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# 求解数的深度（最小深度）
# 与最大深度不同，最小深度需要考虑有未到达叶子节点的情况
# 如果左右子树里有一方为空，则min只能由另一半决定
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


# 验证平衡（左右子树高度差不超过1，且左右子树平衡）
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


# 验证 BST（二叉搜索）


# 验证对称

