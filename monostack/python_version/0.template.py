# monostack template

def convert_to_monostack(nums):
    stack = []
    for i in range(len(nums)):
        while stack and stack[-1] < nums[i]:
        # 单调递减栈，当栈顶小于当前值，需要pop栈顶，保证无增大的情况
            stack.pop()
        # 跳出while循环，要么栈空了，要么栈顶不再小于当前值，可以压栈
        stack.append(nums[i])
    return stack

if __name__ == "__main__":
    nums = [1, 4, 5, 3, 2, 8, 6]
    stack = convert_to_monostack(nums[::-1])
    print(stack)
        

