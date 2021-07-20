# 题目描述
# medium
# 98. 验证二叉搜索树
"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：
    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

====================================================================
题解：
    方法1：构造一个helper函数，传入node和它应该满足的区间[min, max]，本层逻辑就是 min < node.val < max
    递归下去，让所有以该节点为root的子树中的节点都满足范围限制。
    算法的核心：node.left的范围变成[min, node.val]，即最小值服从原限制，而最大值收缩（根据node的值）
            同理，node.right的范围变成[node.val, max]。
    其它部分显然。

    方法2：直接中序遍历，如果是正序，那么就是BST

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 执行用时：32 ms, 在所有 Python 提交中击败了78.89% 的用户
# 内存消耗：17.4 MB, 在所有 Python 提交中击败了71.74% 的用户
class Solution:
    def isValidBST(self, root):
        def inside_range(node, mini, maxi):
            if not node:
                return True
            if node.val > mini and node.val < maxi:
                # 核心操作：递归限制每个节点的值的范围。
                left_check = inside_range(node.left, mini, node.val)
                right_check = inside_range(node.right, node.val, maxi)
                if left_check and right_check:
                    return True 
            return False
        check_all = inside_range(root, -float("inf"), float("inf"))
        return check_all