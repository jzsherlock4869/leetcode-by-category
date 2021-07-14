# backtrack template is as follows

# res 必须是一个全局遍历（如果写成class，应该是一个self.res，便于所有的backtrack都能修改）
res = list()
# backtrack的两个参数是：当前路径
def backtrack(cur_path, cur_arr):
    # 结束条件，满足某种条件，可以将该path加入到最终的res中
    if some_condition:
        # 这里的some_condition比如：len(cur_path) = n，etc.
        res.append(cur_path)
        return
    # 不满足条件，需要树继续向下生长，然后遍历每个子节点，分别递归回溯。
    for i in cur_arr:
        # 这里是递归backtrack，但是path和arr由于选了一个i，会有变化
        new_path = cur_path (some operation) i
        new_arr = cur_path (some operation) i
        backtrack(new_path, new_arr)
        # 注意，这里的new_path不能直接修改掉cur_path，否则需要还原cur_path
        # 因为这里的for循环相当于对各个子节点各自尝试，他们是同层的，不应该相互影响。