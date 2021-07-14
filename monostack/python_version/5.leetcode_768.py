# 题目如下：
# medium
# 768. 最多能完成排序的块 II
"""
数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，并将这些块分别进行排序。
之后再连接起来，使得连接的结果和按升序排序后的原数组相同。
我们最多能将数组分成多少块？

示例 1:

输入: arr = [4,3,2,1,0]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。

示例 2:

输入: arr = [1,0,2,3,4]
输出: 4
解释:
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。

注意:

    arr 的长度在 [1, 10] 之间。
    arr[i]是 [0, 1, ..., arr.length - 1]的一种排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-chunks-to-make-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

=======================================================================

解法：
首先，这个问题到底是在求什么？
将一个arr拆成多块，并且块内部sort得到的结果就是最终的sort结果。如果能满足这一要求，那么必然有对于任意的相邻块：
左max <= 右min
从左到右遍历，如果当前cur大于等于前面subarr的最大值，那么就可以把当前访问过的这部分分成subarr和[cur]两个chunk（当然subarr还可以再划分）。
如果cur不满足，说明它需要与前面的某几chunk进行合并，才能将它放到sort后应在的位置。
最少合并几次呢？我们建立一个stack，其中每个元素都是对应chunk的最大值，将cur与stack.top比较，如果cur小，说明要合并当前的top所对应的chunk，进行pop。
但是这还不一定完全可行，需要继续进一步比较合并后前面的组的最大值与cur的关系，一直比较下去，直到找到一个比cur小的，停下。cur就算merge成功了。
根据上面的分析，这个stack就是一个单调栈，而且是单调递增栈。

需要注意的是：这里的cur与stack.top比较并递归地pop了一堆stack中的元素后，还需要把原来的top放回去。
原因在于：这个pop代表的是合并的过程，而stack元素代表的是合并后的最大值。由于进入push过程的条件就是cur < stack.top，
因此合并后当前chunk的最大值还是原来的top。

结果：
执行用时：24 ms, 在所有 Python 提交中击败了43.90% 的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了68.29% 的用户
"""

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []
        n = len(arr)
        for i in range(n):
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                # stack not empty and cur <= stack.top
                cur_max = stack[-1]
                while stack and stack[-1] > arr[i]:
                    stack.pop(-1)
                stack.append(cur_max)
                # 这里注意：append的是当前的最大值cur_max，而非在移动对比的cur。
                # 只需要理解了这个向左对比pop的过程就是一个从右向左merge各个chunk的过程即不难理解。
                # merge完成后，我们需要保留在stack中的仍只是当前的top，cur既然已经进入pop阶段，说明肯定不是某个chunk的max
                # pop只是为了将cur也能符合规则地加入到最后一个chunk中。
                
        return len(stack)