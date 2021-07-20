# 题目描述
# hard
# 124. 二叉树中的最大路径和
"""
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
路径和 是路径中各节点值的总和。
给你一个二叉树的根节点 root ，返回其 最大路径和 。

示例 1：
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2：
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

提示：
    树中节点数目范围是 [1, 3 * 104]
    -1000 <= Node.val <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

==========================================================================
题解：
    一个树中（从一个node到另个node）的path，按照定义，必然是先上去若干节点，到了最高点，然后下降若干节点。（specifically也包括0个）
    于是定义一个变量f(node)，表示在该node为起点的情况下，该node为根的子树中path的最大和。
    于是，这个变量可以递归的求解：
        如果：f(node.left) < 0，那么将 f(node.left) = 0
        right同理：f(node.right) > 0 ==> f(node.right) < 0 (如果加上子节点的path还不如不加，就把它丢掉)
        递归公式为：f(node) = node.val + max(f(node.left), f(node.right))
    有了这个变量，可以计算以node为最高点的path的最大路径和，即：reward(node) = node.val + f(node.left) + f(node.right)
    最后，对所有的node都遍历到了，于是各种情况都已齐备，对所有node求reward最大即可。（用一个全局变量在递归过程中就可以求出来了）

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path_reward = float('-inf')
        def nodeReward(node):
            if not node:
                return 0
            left_r = max(nodeReward(node.left), 0)
            right_r = max(nodeReward(node.right), 0)
            cur_r = node.val + max(left_r, right_r)
            cur_path_r = node.val + left_r + right_r
            self.max_path_reward = max(self.max_path_reward, cur_path_r)
            return cur_r
        nodeReward(root)
        return self.max_path_reward