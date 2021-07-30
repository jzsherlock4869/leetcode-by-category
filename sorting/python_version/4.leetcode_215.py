# 题目描述
# medium
# 215. 数组中的第K个最大元素
"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

提示：
    1 <= k <= nums.length <= 104
    -104 <= nums[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

======================================================================
题解：
    考虑快排中的根据pivot将数组分成两组的操作，对数组进行排序。由于只需要找到第k大元素
    那么，如果刚好一次partition返回的pivot的位置是k的话，那么即可直接返回，其余部分不用排序。
    在递归调用partition的过程中，由于 左边 < pivot < 右边，因此，根据pivot的位置可以二分查找。

    本质上即一个 快排 + 二分 的任务。
"""

class Solution(object):

    def partition(self, nums, l, r):
        # 传数组引用，实际作用于 nums[l...r] 闭区间
        pivot = nums[l]
        while(l < r):
            while(l < r and nums[r] >= pivot):
                r -= 1
            # 注意，此时已经将pivot所在的位置填上了，r当前指向的元素可以视为一个空缺，暂时不需要交换
            nums[l] = nums[r]
            while(l < r and nums[l] <= pivot):
                l += 1
            # 此时相当于才完成了一次交换。
            nums[r] = nums[l]
        nums[l] = pivot
        return l

    # 类快排的操作（partition加二分）
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def get_topk(nums, l, r):
            if l < r:
                idx = self.partition(nums, l, r)
                if idx == k:
                    return nums[k]
                else:
                    if idx > k:
                        self.partition(l, idx + 1)
                    






















def partition(nums, left, right): 
    pivot = nums[left]
    #初始化一个待比较数据 
    i,j = left, right 
    while(i < j): 
        while(i<j and nums[j]>=pivot): #从后往前查找，直到找到一个比pivot更小的数 
            j-=1 
        nums[i] = nums[j] 
        #将更小的数放入左边 
        while(i<j and nums[i]<=pivot): #从前往后找，直到找到一个比pivot更大的数 
            i+=1 
        nums[j] = nums[i] 
        #将更大的数放入右边 
        #循环结束，i与j相等 
    nums[i] = pivot #待比较数据放入最终位置 
    return i #返回待比较数据最终位置 
