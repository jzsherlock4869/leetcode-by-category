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

| 题目                                                         | 解法                    | 关键点                                                       |
| ------------------------------------------------------------ | ----------------------- | ------------------------------------------------------------ |
| [template](./binary_tree/python_version/0.template.py)       | 二叉树基本操作          | template                                                     |
| [103. 二叉树的锯齿形层序遍历](./binary_tree/python_version/1.leetcode_103.py) | 层序遍历、双端队列      | 普通层序遍历基础上对不同层进行区分                           |
| [235. 二叉搜索树的最近公共祖先](./binary_tree/python_version/17.leetcode_235.py) | 二叉查找+返回规则       | BST的特性，分裂点在node.val与p和q不同大于或小于的位置。      |
| [236. 二叉树的最近公共祖先](./binary_tree/python_version/2.leetcode_236.py) | 递归                    | 边界条件（node.val==p or q），本层逻辑：右null返回左（左null同理）；同时null返回null；同时非null返回自身。 |
| [199. 二叉树的右视图](./binary_tree/python_version/3.leetcode_199.py) | DFS（中右左）、层序遍历 | DFS时只保留本层第一个、层序遍历分层输出取最右。              |
| [102. 二叉树的层序遍历](./binary_tree/python_version/4.leetcode_102.py) | 层序遍历分层输出        | 模板题。只需注意while que + for i in range(len(que))，其它显然。 |
| [94. 二叉树的中序遍历](./binary_tree/python_version/7.leetcode_94.py) | 递归、迭代、Morris      | 模板题。                                                     |
| [98. 验证二叉搜索树](./binary_tree/python_version/8.leetcode_98.py) | 递归、遍历              | 设计helper(node, min, max)函数，对每个node递归做范围限制。   |
| [105. 从前序与中序遍历序列构造二叉树](./binary_tree/python_version/5.leetcode_105.py) | 递归                    | 前序找根节点，分割中序遍历结果。递归建树                     |
| [124. 二叉树中的最大路径和](./binary_tree/python_version/6.leetcode_124.py) | 递归                    | path总有一个顶点，递归计算每个顶点为起点的路径，构造出path   |
| [99. 恢复二叉搜索树](./binary_tree/python_version/9.leetcode_99.py) | 中序遍历                | 中序遍历，利用BST在中序遍历的顺序性，进行判断                |
| [100. 相同的树](./binary_tree/python_version/10.leetcode_100.py) | 递归                    | check本层val、递归check左子树、递归check右子树               |
| [101. 对称二叉树](./binary_tree/python_version/11.leetcode_101.py) | 递归                    | 设计helper(node1, node2)，内侧外侧分别递归                   |
| [104. 二叉树的最大深度](./binary_tree/python_version/12.leetcode_104.py) | 递归                    | 模板题。                                                     |
| [110. 平衡二叉树](./binary_tree/python_version/13.leetcode_110.py) | 递归                    | 借助depth函数，check本层的高度差 and 左子树平衡 and 右子树平衡 |
| [111. 二叉树的最小深度](./binary_tree/python_version/14.leetcode_111.py) | 递归                    | 当node无左子树或者无右子树时，min depth取决于另一边（有子树的部分） |
| [112. 路径总和](./binary_tree/python_version/15.leetcode_112.py) | 递归                    | 当node为叶子，路径满足条件时，返回True并退出，否则False，递归左右子树 |
| [113. 路径总和 II](./binary_tree/python_version/16.leetcode_113.py) | 递归（回溯）            | 维护一个res列表，每个符合的path加入res。dfs步骤：path.push(val) -> recursive dfs -> path.pop(val) |



#### 动态规划（Dynamic Programming）

| 题目                                                         | 解法                 | 关键点                                                       |
| ------------------------------------------------------------ | -------------------- | ------------------------------------------------------------ |
| template                                                     | 动态规划             | template                                                     |
| [5. 最长回文子串](./dynamicprogramming/1.leetcode_5.py)      | 动态规划、中心点扩展 | 根据s[i...j]的起止位置建立dp矩阵；只有1/2/3个元素的base case；填充顺序。 |
| [10. 正则表达式匹配](./dynamicprogramming/2.leetcode_10.py)  | 动态规划             | 当无star时，简单递归；有star时分类讨论（匹配0次；匹配多次）  |
| [32. 最长有效括号](./dynamicprogramming/4.leetcode_32.py)    | 动态规划             | 考察当前位置的上一个，如果“(”直接匹配，如果“)”找到合法括号前面的，看是否是“(”。 |
| [44. 通配符匹配](./dynamicprogramming/6.leetcode_44.py)      | 动态规划             | 如果match，dp(i, j) = dp(i-1, j-1)；否则如果有star，dp(i, j) = dp(i-1, j) or dp(i, j-1) |
| [53. 最大子序和](./dynamicprogramming/7.leetcode_53.py)      | 动态规划             | 动态规划例题 dp(i) = max(dp(i-1) + nums[i], nums[i])，即前面的正向加上，负向舍弃。 |
| [70. 爬楼梯](./dynamicprogramming/8.leetcode_70.py)          | 动态规划             | 例题，斐波那契的递推关系                                     |
| [72. 编辑距离](./dynamicprogramming/9.leetcode_72.py)        | 动态规划             | 考虑增、替、删、无四种可能的操作，构造递推关系。             |
| [121. 买卖股票的最佳时机](./dynamicprogramming/11.leetcode_121.py) | 遍历更新、动态规划   | 【单次买卖】如果i时刻卖出，最大差价为prices(i) - min (prices(j))，j <= i。最后取所有卖出时刻最大差价的最大值。 |
| [122. 买卖股票的最佳时机 II](./dynamicprogramming/12.leetcode_122.py) | 动态规划             | 【多次买卖】每个时刻两种状态：持有/不持有股票。递推即可。    |
| [123. 买卖股票的最佳时机 III](./dynamicprogramming/13.leetcode_123.py) | 动态规划             | 【两次买卖】dp为n x 4的矩阵，4列分别表示当前状态：买一次，买卖一次，买卖一次又买一次，买卖两次。建立递推关系 |
| [221. 最大正方形](./dynamicprogramming/17.leetcode_221.py)   | 动态规划             | dp(i, j) = min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1))         |
| [139. 单词拆分](./dynamicprogramming/14.leetcode_139.py)     | 动态规划             | 考虑dp[i]表示末尾为s[i]的单词，向前查找，如果有一个单词s(j...i)符合，那么考察dp[j-1]的True or False，否则dp[i] = False。返回的结果为dp[-1]。 |
| [152. 乘积最大子数组](./dynamicprogramming/15.leetcode_152.py) | 动态规划             | 关键：正负值分类讨论，dp为两列，根据nums[i]的正负进行判断和转移。 |
|                                                              |                      |                                                              |
|                                                              |                      |                                                              |
|                                                              |                      |                                                              |
|                                                              |                      |                                                              |







