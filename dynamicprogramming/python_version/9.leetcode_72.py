# 题目描述
# hard
# 72. 编辑距离
"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
    插入一个字符
    删除一个字符
    替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

提示：
    0 <= word1.length, word2.length <= 500
    word1 和 word2 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

===========================================================
题解：
    考虑dp[i][j]表示word1前i个字符和word2前j个字符的编辑距离，那么可以建立如下递推关系：
    - 一般来说，按照操作：
        word1插入：dp[i][j] = dp[i][j-1] + 1; 
        word1替换：dp[i][j] = dp[i-1][j-1] + 1;
        word1删除：dp[i][j] = dp[i-1][j] + 1;
        最终因为是求距离，于是对上述情况取min即可。
    - 如果word1[i-1] == word2[j-1]，即当前字符相等，那么编辑可以距离不变，dp[i][j] = dp[i-1][j-1]；也可以操作。

"""

# 速度和内存开销都很大，速度可以通过简并递推关系改进，内存可以改成动态的，隐式的dp矩阵。
# 执行用时：136 ms, 在所有 Python 提交中击败了52.64% 的用户
# 内存消耗：16.4 MB, 在所有 Python 提交中击败了29.88% 的用户
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # 初始化
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(m + 1):
            dp[i][0] = i
        # 按行填充
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                min_dist = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
                if word1[i - 1] == word2[j - 1]:
                    min_dist = min(min_dist, dp[i - 1][j - 1])
                dp[i][j] = min_dist
        return dp[m][n]
