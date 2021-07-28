# 常用的排序

# 归并排序

# 快速排序
def quicksort(nums, l, r):
    pivot = nums[l]
    i, j = l, r
    while(i < j):
        while(i < j and nums[j] <= pivot):
            