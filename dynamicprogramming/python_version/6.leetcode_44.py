# 题目描述
# hard
# 44. 通配符匹配
"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。

两个字符串完全匹配才算匹配成功。
说明:
    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。

示例 3:
输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

示例 4:
输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

示例 5:
输入:
s = "acdcb"
p = "a*c?b"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wildcard-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

=============================================================
题解：
    主要还是构造递推公式。【通配符】和之前的【正则表达式】类似，
    区别在于star不是和前面的char有关系的，因此相对re通配符的递推关系更简单。
    dp[i][j]表示第s[i-1]和p[j-1]的匹配关系，那么分类讨论如下：
    - 如果p[j-1] == "?" or s[i-1] == p[j-1]: 说明当前匹配，转移方程：
        dp[i][j] = dp[i-1][j-1]
    - 如果p[j-1] == "*"，考虑匹配零次（[i][j-1]）和1到多次（[i-1][j]），转移方程：
        dp[i][j] = dp[i][j-1] or dp[i-1][j]
    
    初始化：
    首先置为False。
    dp[0][j]和dp[i][0]对应s为空串和p为空串的情况，自然地，dp[i][0] = False
    而s为空时，如果p[...j]都是star，才能有dp[0][j] = True，否则false。（遇到第一个不是star的，停止赋值True）

"""

# 执行用时：944 ms, 在所有 Python 提交中击败了13.98% 的用户
# 内存消耗：21.5 MB, 在所有 Python 提交中击败了25.85% 的用户
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def match(si, pi):
            if pi == "?":
                return True
            else:
                return si == pi
        m, n = len(s), len(p)
        # 初始化 dp 矩阵
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True # 两者都是空串，匹配
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = True
            else:
                break
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if match(s[i - 1], p[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j - 1] == "*":
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1] # 匹配1-多次；匹配0次
        return dp[m][n]
