# 题目如下：
# easy
# 496. 下一个更大元素 I
"""

给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。


示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

示例 2:

输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
    对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

 

提示：

    1 <= nums1.length <= nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 104
    nums1和nums2中所有整数 互不相同
    nums1 中的所有整数同样出现在 nums2 中

 

进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

============================================================================

解法：对于nums2，依次找到next greater number，存成hash表，在用nums1中的每个元素依次查表即可。
next greater number类的题目，优先考虑单调栈（monostack），单调栈求解数组各元素的next greater是线性复杂度。

结果：执行用时：16 ms, 在所有 Python 提交中击败了96.52% 的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了55.22% 的用户
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greater_nums = [-1 for i in range(len(nums2))] # 初始化用-1，这样stack空时就不用操作了
        for i in range(len(nums2)):
            revi = len(nums2) - 1 - i # 向右边找下个更大，因此需要从后往前遍历，并且建立递减栈
            while stack and nums2[revi] > stack[-1]:
                stack.pop(-1)
            if stack:
                # 在这里输出next greater的值，即当时的栈顶元素
                next_greater_nums[revi] = stack[-1]
            stack.append(nums2[revi])
        # 建立hash表，用于给nums1查找
        hashmap = dict([(nums2[k], next_greater_nums[k]) for k in range(len(nums2))])
        res = []
        for num in nums1:
            res.append(hashmap[num])
        return res
