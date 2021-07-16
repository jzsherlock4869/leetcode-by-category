# leetcode solutions organized by categories

按照类别整理的leetcode题解，附类别模板和题目分析。



#### 单调栈（monostack）

| 题目                                                         | 解法   | 关键点                                               |
| ------------------------------------------------------------ | ------ | ---------------------------------------------------- |
| [template](./monostack/python_version/0.template.py)         | 单调栈 | template                                             |
| [496. 下一个更大元素 I](./monostack/python_version/1.leetcode_496.py) | 单调栈 | 单调栈典型例题，对每个元素右向删小于它的，构成单减栈 |
| [1475. 商品折扣后的最终价格](./monostack/python_version/2.leetcode_1475.py) | 单调栈 | next greater 的简单变形                              |
| [739. 每日温度](./monostack/python_version/3.leetcode_739.py) | 单调栈 | next greater 的简单变形                              |
| [503. 下一个更大元素 II](./monostack/python_version/4.leetcode_503.py) | 单调栈 | 同496，同时记录位置                                  |
| [768. 最多能完成排序的块 II](./monostack/python_version/5.leetcode_768.py) | 单调栈 | 内部排序等价于整体排序的条件：左块最大<=右块最小     |



#### 回溯法（backtracking）

| 题目                                                         | 解法   | 关键点                                              |
| ------------------------------------------------------------ | ------ | --------------------------------------------------- |
| [template](./backtrack/python_version/0.template.py)         | 回溯法 | template                                            |
| [17. 电话号码的字母组合](./backtrack/python_version/1.leetcode_17.py) | 回溯法 | 标准回溯问题（hash+dfs）                            |
| [22. 括号生成](./backtrack/python_version/2.leetcode_22.py)  | 回溯法 | 左右括号数量各自参数                                |
| [39. 组合总和](./backtrack/python_version/3.leetcode_39.py)  | 回溯法 | target作为return条件                                |
| [40. 组合总和 II](./backtrack/python_version/4.leetcode_40.py) | 回溯法 | target作为return条件，组合问题需要排序去重          |
| [46. 全排列](./backtrack/python_version/5.leetcode_46.py)    | 回溯法 | 标准回溯模板，无剪枝                                |
| [47. 全排列 II](./backtrack/python_version/6.leetcode_47.py) | 回溯法 | 树的同层要去重（方法：排序后连续相同只保留一个）    |
| [51. N 皇后](./backtrack/python_version/7.leetcode_51.py)    | 回溯法 | 回溯经典例题，冲突函数定义                          |
| [77. 组合](./backtrack/python_version/8.leetcode_77.py)      | 回溯法 | 选/不选 第i个元素为两子节点，各自回溯。组合需去重。 |
| [78. 子集](./backtrack/python_version/9.leetcode_78.py)      | 回溯法 | 幂集需要路径上的节点全部return                      |



#### 二叉树（binary tree）







