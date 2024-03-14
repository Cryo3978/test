#designed by Shuheng Chen, Tianjin University
#此问题为经典问题，用stack解决较为简洁
def check_brackets(test_cases):
    for line in test_cases:
        # 用于存储未匹配的左括号
        stack = []
        # 初始化标记列表，初始为空格
        marks = [' '] * len(line)

        for i, char in enumerate(line):
            if char == '(':
                # 将左括号的索引推入栈中
                stack.append(i)
            elif char == ')':
                if stack:
                    # 弹出一个左括号以匹配当前的右括号
                    stack.pop()
                else:
                    # 没有左括号可以匹配，标记 '?'
                    marks[i] = '?'

        # 遍历完成后，栈中剩余的没有右括号匹配的左括号的索引对应的位置需要标记 'x'
        for idx in stack:
            marks[idx] = 'x'

        print(line)  # 打印原始字符串
        print(''.join(marks))  # 打印标记结果

# 测试用例，根据邮件中的案例
test_cases = [
    "bge)))))))))",
    "((IIII)))))",
    "()()()()(uuu",
    ")))UUUU((()"
]
check_brackets(test_cases)

