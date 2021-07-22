# 题目描述
# medium
# 221. 最大正方形
"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

示例 1：
输入：matrix = [["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]]
输出：4

示例 2：
输入：matrix = [["0","1"],["1","0"]]
输出：1

示例 3：
输入：matrix = [["0"]]
输出：0

提示：
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] 为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

===========================================================
题解：
    此题关键在于理解正方形约束的作用。我们构造dp矩阵，其中dp[i][j]表示以[i,j]为右下角的最大的正方形边长。
    那么，如果dp[i][j] = m，它实际上的意思是，从[i,j]出发，只能向左或向上移动，最多走m步，就一定会遇到一个0。
    换句话说，如果想要路径里都是1，只能走m步。
    基于这个理解，即dp[i][j]实际上代表着第一次走到0的步数，那么递推关系也就好理解了。
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    min中的三个部分分别代表：向上走最大走 dp[i-1][j] + 1 步；向左走最多...步；向左上方走最多...步。
    要求的就是各种路径都满足的最多可以走的步数，因此由最短的来决定，于是取了min

"""

# 执行用时：56 ms, 在所有 Python 提交中击败了91.15% 的用户
# 内存消耗：18.6 MB, 在所有 Python 提交中击败了44.26% 的用户
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxi = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                    maxi = max(maxi, dp[i][j])
        return maxi * maxi
