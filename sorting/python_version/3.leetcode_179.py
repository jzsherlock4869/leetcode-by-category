# 题目描述
# medium
# 179. 最大数

"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：
输入：nums = [10,2]
输出："210"

示例 2：
输入：nums = [3,30,34,5,9]
输出："9534330"

示例 3：
输入：nums = [1]
输出："1"

示例 4：
输入：nums = [10]
输出："10"

提示：
    1 <= nums.length <= 100
    0 <= nums[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

====================================================

题解：
    其实还是一个排序问题，考虑到这个序应该怎样定义，才能使得最终拼接出来的结果最大。
    对于几个非负整数，比如 11, 12, 1, 110。 如果取11和12，那么显然12应该放在前面，原因是1211 > 1112。
    同理，1和110，应该1放在110前面，因为1110 > 1101。都按照这个方式，即可形成偏序关系。
    只要前面的数（按该规则）都应该在后面的数之前，那么得到的拼接结果就是最大的。

"""

# 执行用时：24 ms, 在所有 Python 提交中击败了88.33% 的用户
# 内存消耗：12.8 MB, 在所有 Python 提交中击败了97.14% 的用户
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        res = "".join(nums)
        # 这是题目中的一些trivial case，当多个0时，只输出一个。加了个规则判断。
        if res.startswith("0"):
            res = "0"
        return res