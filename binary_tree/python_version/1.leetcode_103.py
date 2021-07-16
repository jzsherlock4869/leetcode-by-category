# 题目描述
# medium
# 103. 二叉树的锯齿形层序遍历
"""
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

返回锯齿形层序遍历如下：
[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

===================================================================================
题解：
    方法1（简单）：判断层数，遍历完成后，奇数层翻转（设root为0层）
    方法2：双端队列。可以右进左出，也可左进右出。不同奇偶的层入队列方向相反。

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 执行用时：12 ms, 在所有 Python 提交中击败了97.66% 的用户
# 内存消耗：13.5 MB, 在所有 Python 提交中击败了6.15% 的用户
# 分层进行层序遍历，需要reversed进行反向输出。
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = list()
        que = [root]
        reverse = False
        while que:
            nxt_layer = []
            cur_layer_vals = []
            if reverse:
                cur_layer_vals = [n.val for n in que[::-1]]
            else:
                cur_layer_vals = [n.val for n in que]
            res.append(cur_layer_vals)
            for i in range(len(que)):
                cur_node = que[i]
                if cur_node.left:
                    nxt_layer.append(cur_node.left)
                if cur_node.right:
                    nxt_layer.append(cur_node.right)
            que = nxt_layer
            reverse = not reverse
        return res
