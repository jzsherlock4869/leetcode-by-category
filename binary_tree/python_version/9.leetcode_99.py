# 题目描述
# medium
# 99. 恢复二叉搜索树
"""
给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。
进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？

示例 1：
输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。

示例 2：
输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。

提示：
    树上节点的数目在范围 [2, 1000] 内
    -231 <= Node.val <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

========================================================================

题解：
    方法 1：中序遍历打印出来，存成list，找到错序的两个元素，进行交换。（常规思路，不写了）
    方法 2：直接在中序遍历的过程中，将当前node.val与prev_node.val比较，找到第一个和第二个错序的node，
            第一个prev_node.val > node.val的，前面的是错序的node（因为中序遍历先处理val小的那组，所以出现大的是错的）
            第二个则后面是错序。只需要记录这两个node即可。

"""

# 方法 2
# 执行用时：68 ms, 在所有 Python 提交中击败了55.07% 的用户
# 内存消耗：13.2 MB, 在所有 Python 提交中击败了94.93% 的用户

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.target_1, self.target_2 = None, None
        self.prev_node = TreeNode(val=-float("inf"))
        def inorder_traverse(node):
            if not node:
                return
            inorder_traverse(node.left)
            # 核心逻辑：在中序遍历的本层逻辑中进行判断，如果遇到逆序的就记录下来
            if not self.target_1 and self.prev_node.val > node.val:
                self.target_1 = self.prev_node
            if self.target_1 and self.prev_node.val > node.val:
                self.target_2 = node
            # 注意更新prev_node
            self.prev_node = node
            # 本层逻辑结束。
            inorder_traverse(node.right)
        inorder_traverse(root)
        # python中的一种简便的交换方式：a, b = b, a
        self.target_1.val, self.target_2.val = self.target_2.val, self.target_1.val
        return root
        