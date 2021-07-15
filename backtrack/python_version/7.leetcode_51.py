# 题目描述
# hard
# 51. N 皇后
"""
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 

示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]

提示：
    1 <= n <= 9
    皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

==============================================================
题解：
    n皇后是回溯法的经典问题。
    关键1：如何判断冲突。
    关键2：backtrack + 冲突剪枝

"""

# 执行用时：44 ms, 在所有 Python 提交中击败了69.68% 的用户
# 内存消耗：13.2 MB, 在所有 Python 提交中击败了93.79% 的用户
class Solution(object):
    # 采用了一个巧妙的记录法，用长度为n的list表示棋盘
    # 由于n皇后不可能出现一行多个，所以一个item表示一行皇后的列号
    def check_valid(self, part, x):
        idx = len(part)
        # 不同一列
        if x in part:
            return False
        # 不在对角线
        for i, p in enumerate(part):
            if idx + x == i + p or idx - x == i - p:
                return False
        # 记法已经保证了不同行
        return True

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = list()
        # backtrack的参数可以只用path即可。
        def backtrack(path):
            if len(path) == n:
                res.append(path)
                return path
            idx = len(path)
            for i in range(n):
                if not self.check_valid(path, i):
                    continue
                new_path = path + [i]
                backtrack(new_path)
        backtrack([])
        # 注意，按照题目要求，还要把棋盘格画出来
        ret = []
        for solution in res:
            checkboard = []
            for col_id in solution:
                row = "." * col_id + "Q" + "." * (n - col_id - 1)
                checkboard.append(row)
            ret.append(checkboard)
        return ret