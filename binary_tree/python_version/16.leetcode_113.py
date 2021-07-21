# 题目描述
# medium
# 113. 路径总和 II
"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，
找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
叶子节点 是指没有子节点的节点。

示例 1：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]

示例 2：
输入：root = [1,2,3], targetSum = 5
输出：[]

示例 3：
输入：root = [1,2], targetSum = 0
输出：[]

提示：
    树中节点总数在范围 [0, 5000] 内
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

==============================================================
题解：
    和前面的路径和题目写法类似，只是上一个需递归返回True or False，这里需维护一个res list
    res list的更新方法和backtrack的模板一样，先path.append(val)，然后dfs，然后path.pop(val)。
    如果再过程中满足条件，就将path加入res list中。

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.res = list()
        self.path = list()
        def dfs(node, target):
            if not node:
                return
            self.path.append(node.val)
            if not node.left and not node.right:
                if node.val == target:
                    # 注意！！！后面用了path.pop()，因此这里的append必须append path[:]
                    # 如果想避免这个问题，需在后面用path = path[:-1]代替pop操作
                    self.res.append(self.path[:])
            dfs(node.left, target - node.val)
            dfs(node.right, target - node.val)
            self.path.pop(-1)
        dfs(root, targetSum)
        return self.res
