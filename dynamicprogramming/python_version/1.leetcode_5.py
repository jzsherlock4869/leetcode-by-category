# 题目描述
# medium
# 5. 最长回文子串
"""
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

示例 3：
输入：s = "a"
输出："a"

示例 4：
输入：s = "ac"
输出："a"

提示：
    1 <= s.length <= 1000
    s 仅由数字和英文字母（大写和/或小写）组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

=====================================================================
题解：
    考虑动态规划，建立dp矩阵，其中dp[i][j] 表示s[i...j]（闭区间）是否是回文字串。
    基本递推关系：dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
    接下来就是一些base case，比如，i > j 时不用考虑，i == j 时直接为True
    另外，在s[i] == s[j] 的情况下，如果j == i + 1（去掉首尾为空） or j == i + 2（去掉首尾为单个元素），也为True
    （这个base case是为了处理 i+1 > j-1 的情况，即递推关系中的上一步的值不存在，其实j == i + 2也可以不用）

    注意！！！dp的递推方向是从左下到右上方，因此需要逐列填充！！！
"""

# 执行用时：5536 ms, 在所有 Python 提交中击败了43.79% 的用户
# 内存消耗：21.6 MB, 在所有 Python 提交中击败了5.93% 的用户
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = 1
        longest_str = s[0]
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        # 初始化dp矩阵
        for i in range(n):
            dp[i][i] = True
        # 注意！先j后i，保证左下角填好后再填右上角
        for j in range(1, n):
            for i in range(j):
                if s[i] != s[j]:
                    continue
                else:
                    # base case，直接置为True
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        # 循环不变式
                        dp[i][j] = dp[i + 1][j - 1]
                # 更新longest与对应的回文串
                if dp[i][j] and j - i + 1 > longest:
                    longest_str = s[i: j+1]
                    longest = j - i + 1
        return longest_str

