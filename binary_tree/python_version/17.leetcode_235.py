# 题目描述
# easy
# 235. 二叉搜索树的最近公共祖先
"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

示例 1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。

示例 2:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

说明:
    所有节点的值都是唯一的。
    p、q 为不同节点且均存在于给定的二叉搜索树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

==============================================================================
题解：
    解法1（暴力解法）：先进行搜索，然后记录到p和q的分别的path，找到第一个值不同的点。
    解法2（考虑BST的特点）：p和q的最深的公共父亲是将他们分成两子树的那个node（也可以是一个root一个子树），
                        加判断即可一遍求解，节省存储的path的空间。

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 解法 1
# 执行用时：52 ms, 在所有 Python 提交中击败了96.96% 的用户
# 内存消耗：20.7 MB, 在所有 Python 提交中击败了85.16% 的用户
class Solution(object):

    # BST查找元素的标准模板代码
    def find_path(self, root, target):
        cur_node = root
        path = [root]
        while cur_node.val != target:
            if cur_node.val < target:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left
            path.append(cur_node)
        return path

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path_p = self.find_path(root, p.val)
        path_q = self.find_path(root, q.val)
        ancestor = None
        # 直接比较，找到最深的一个节点
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i].val == path_q[i].val:
                ancestor = path_p[i]
            else:
                break
        return ancestor

        
# 解法 2
# 执行用时：60 ms, 在所有 Python 提交中击败了81.79% 的用户
# 内存消耗：20.6 MB, 在所有 Python 提交中击败了95.95% 的用户
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        cur_node = root
        while (cur_node.val > p.val and cur_node.val > q.val) \
                or (cur_node.val < p.val and cur_node.val < q.val):
            if cur_node.val > p.val:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return cur_node