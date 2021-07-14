# 题目如下
# medium
# 17. 电话号码的字母组合
""" 
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]

提示：
    0 <= digits.length <= 4
    digits[i] 是范围 ['2', '9'] 的一个数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

=============================================================================

题解：
转化成dfs的backtrack问题，这是一个典型且simple的例子，没有prun，所有树的路径都可以加入res。
对比template，path是当前的字母string，arr是剩下的digit string，for循环遍历的是当前的digit对应的各个字母，
for循环对path和arr的改变就是令path增加了一个字母，arr少了一个数字。
这个是backtrack函数，主函数中，初始化，path为空，arr为所有digits，res设置成global的即可。


执行用时：12 ms, 在所有 Python 提交中击败了95.29% 的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了27.47% 的用户
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 按照要求设置边界值
        if not digits:
            return []
        self.set_mapping()
        res = list()
        # 初始情况，path是空，arr是满，res定义在外面，对于backtrack是一个global的变量，用于记录所有可行的path
        self.backtrack("", digits, res)
        return res


    def set_mapping(self):
        self.kv = {
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"
                }
    
    def backtrack(self, path, arr, res):
        # 退出条件，遍历完数字字符串即可
        if arr == "":
            res.append(path)
            return
        # 这里注意，路径增加要按arr的顺序来，子节点就是各个digit对应的字母候选
        for v in self.kv[arr[0]]:
            new_path = path + v
            new_arr = arr[1:]
            self.backtrack(new_path, new_arr, res)