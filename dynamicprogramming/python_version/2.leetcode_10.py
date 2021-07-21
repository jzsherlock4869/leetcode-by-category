# 题目描述
# hard
# 10. 正则表达式匹配
"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

示例 1：
输入：s = "aa" p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

示例 2:
输入：s = "aa" p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3：
输入：s = "ab" p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4：
输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5：
输入：s = "mississippi" p = "mis*is*p*."
输出：false

提示：
    0 <= s.length <= 20
    0 <= p.length <= 30
    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
    保证每次出现字符 * 时，前面都匹配到有效的字符

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

=============================================================================
题解：
    容易想到，dp[i][j]表示s[:i+1]与p[:j+1]的匹配情况（index加1是为了给s和p首部各加一个空格，便于初始化），
    本题的主要难点在于构造递归公式：
    首先总体分为两大类情况：
    1. 没有 star（p[j] != '*'）：
        - 如果s[i] == p[j]，即当前匹配，那么结果递归地取决于之前的dp[i-1][j-1]
        - 如果s[i] != p[j]，即当前不匹配，那么直接返回False
    2. 有 star（p[j] == '*'）：
        2.1 任何情况下，star和前面的char匹配 0 次：
            - dp[i][j] = dp[i][j-2] # 相当于直接删除了pattern中的 char + star的组合
        2.2 当 s[i] == p[j-1] 时，star和前面的char还可以匹配 1到多次：
            - dp[i][j] = dp[i-1][j] # 既然允许匹配多次，匹配掉s中的一个s[i]不影响pattern，还是p[:j+1]
    根据上述递推关系，填充dp矩阵即可。

    注意！将s和p都在首端加一个空字符，则初始化dp[0][0] = True，其他的dp[0][j]或者dp[i][0]都是False

"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        self.s, self.p = s, p
        def matcher(i, j):
            if i == 0:
                return False
            if self.p[j-1] == '.':
                return True 
            return self.s[i-1] == self.p[j-1]
        # 注意！初始化为 (m+1) x (n+1) 的全False矩阵
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        # 空串和空串可以匹配
        dp[0][0] = True
        # 注意 j 需要从 1 开始遍历，因为j=0的必然是False（空串作为模式串，任何s都无法匹配）
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != "*":
                    if matcher(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 2]
                    if matcher(i, j - 1):
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
        return dp[m][n]

