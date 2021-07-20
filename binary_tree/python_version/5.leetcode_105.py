# 题目描述
# medium
# 105. 从前序与中序遍历序列构造二叉树
"""
给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。

示例 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

示例 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

提示:
    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder 和 inorder 均无重复元素
    inorder 均出现在 preorder
    preorder 保证为二叉树的前序遍历序列
    inorder 保证为二叉树的中序遍历序列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

===============================================================================
题解：
    根据preorder表达式，取出第一个元素，即为根节点，然后再从inorder中找到这个节点，划分左右子树。
    容易看出，划分后的结果具有与原问题相同的形式，因此可以递归操作。
    注意！！！这里的递归过程没有对preorder分成左右子树，因为递归完成左子树后，preorder的所有左子树上的node都已经pop出去。


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 执行用时：88 ms, 在所有 Python 提交中击败了72.19% 的用户
# 内存消耗：50.6 MB, 在所有 Python 提交中击败了67.60% 的用户

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 如果为空，直接返回None，对于叶子节点也符合下面的规则
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])
            # python的list类型，slice中的idx超限是允许的，会返回一个[]。
            # (直接的index是不许超限的，有IndexError: list index out of range)
            root.left = self.buildTree(preorder, inorder[:idx])
            # 这里的preorder不需要特殊的处理（比如对应inorder分成两份），
            # 因为递归调用，上面的这句针对root的左子树的操作完成后，自然preorder只剩下右子树了。
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root