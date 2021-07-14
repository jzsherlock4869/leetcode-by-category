# 题目描述
# medium
# 22. 括号生成
"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]

提示：
    1 <= n <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

==============================================================================
题解：
每次节点就是左右括号，二叉树。套用template格式，在backtrack之前进行剪枝，最后加入res是进行验证正确性。
按照标准backtrack格式的结果如解法1，但是效率很低。
执行用时：80 ms, 在所有 Python 提交中击败了8.47% 的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了11.18% 的用户

提高效率：关键在于找到剪枝条件。
如果左括号数量不大于 n，我们可以放一个左括号。
如果右括号数量小于左括号的数量，我们可以放一个右括号。
但是每次查左右括号分别的个数是费时的，因此可以将backtrack函数改造一下，把l和r作为两个变量分别传入，代替n。如解法2。
执行用时：20 ms, 在所有 Python 提交中击败了74.27% 的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了63.03% 的用户

"""


# 解法 1 
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = list()
        self.backtrack("", 2 * n, res)
        return res
    
    # 提前中止（prun）的一个标准
    def check_valid(self, paren):
        stack = []
        for p in paren:
            if p == "(":
                stack.append(p)
            else:
                if not stack:
                    return False
                if not stack[-1] == "(":
                    return False
                stack = stack[:-1]
        return True

    # backtrack主函数，完全按照template。path和arr（这里的arr变成了剩下的字符数量，作用是一样的）
    def backtrack(self, path, n, res):
        # 完成一个路径，符合要求就返回
        if n == 0:
            if path.count("(") == len(path) // 2 and path.count(")") == len(path) // 2:
                res.append(path)
            return
        # 没有完成路径，继续找子节点，递归回溯
        for i in ["(", ")"]:
            new_path = path + i
            new_n = n - 1
            if not self.check_valid(new_path):
                return
            self.backtrack(new_path, new_n, res)


# 解法 2
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = list()
        # 在函数内定义，参数量更少，而且也不用带上全局的res
        # 这里的path表示路径，l和r分别表示已经有了几个左括号和有括号
        def backtrack(path, l, r):
            if l == n and r == n:
                res.append(path)
                return
            # 左括号还不到n，可以加左括号
            if l < n:
                new_path = path + "("
                backtrack(new_path, l+1, r)
            # 右括号小于左括号，就可以加右括号
            # 注意，这里的两个if并列，相互不影响。
            if r < l:
                new_path = path + ")"
                backtrack(new_path, l, r+1)
                
        backtrack("", 0, 0)
        return res