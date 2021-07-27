# 题目描述
# medium
# 148. 排序链表

"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
进阶：
    你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]

提示：
    链表中节点的数目在范围 [0, 5 * 104] 内
    -105 <= Node.val <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

============================================================
题解：
    链表考虑用归并排序。主要分为两个函数，一个merge，一个二分。
    将链表拆分成两部分，考虑快慢指针。
    将排好序的链表合并，这个步骤和数组类似，直接将两个链表按顺序遍历链接成一个即可。

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 执行用时：532 ms, 在所有 Python 提交中击败了19.01% 的用户
# 内存消耗：42 MB, 在所有 Python 提交中击败了85.78% 的用户
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # merge函数，将两个linked list按顺序merge起来，标准模板：
        def merge(head1, head2):
            dummy_node = ListNode(0)
            pt1, pt2 = head1, head2
            pt = dummy_node
            while pt1 and pt2:
                if pt1.val > pt2.val:
                    pt.next = pt2
                    pt2 = pt2.next
                else:
                    pt.next = pt1
                    pt1 = pt1.next
                pt = pt.next
            pt.next = pt1 if pt1 else pt2
            return dummy_node.next
        # sorter函数，用来处理二分以及分别的sort（递归），其中二分用了快慢指针。
        def sorter(start):
            if not start:
                return None
            if start.next == None:
                return start
            # 快慢指针初始化，分别指向第1和2个，后续slow：1，2，3，...；fast：2，4，6，...
            slow, fast = start, start.next
            # 跳出循环的条件：fast is None (奇数个元素，倒数第二直接到null)，或者 fast.next is None（偶数个元素，到了末尾节点）
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            # slow 指向第 n // 2 个元素，因此mid为next
            mid = slow.next
            slow.next = None
            return merge(sorter(start), sorter(mid))
        return sorter(head)

