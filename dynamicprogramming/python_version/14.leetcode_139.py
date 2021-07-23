# 题目描述
# medium
# 139. 单词拆分
"""
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
    拆分时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

=============================================================================================
题解：
    建立dp数组，dp[i]表示s[...i]能否被拆分成dict中的单词。
    于是递推关系可以建立：
        dp[i] = OR (dp[j-1] and s[j...i] in dict)
    也就是说，对于所有以s[i]为结尾的单词，分别作为最后一个单词，看去掉这个单词后，前面能否形成一个合法拆分。

"""


# 执行用时：20 ms, 在所有 Python 提交中击败了94.42% 的用户
# 内存消耗：12.9 MB, 在所有 Python 提交中击败了94.76% 的用户
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        diction = set(wordDict)
        lens = [len(i) for i in diction]
        min_len, max_len = min(lens), max(lens)
        n = len(s)
        dp = [False for _ in range(n)]
        if s[0] in diction:
            dp[0] = True
        for i in range(1, n):
            for j in range(i + 1):
                cur_len = i - j + 1
                if cur_len > max_len or cur_len < min_len:
                    continue
                if s[j: i + 1] in diction:
                    if j - 1 < 0:
                        dp[i] = True
                    else:
                        dp[i] = dp[j - 1]
                    if dp[i] == True:
                        break
        return dp[n-1]
