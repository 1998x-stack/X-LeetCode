from typing import List

def calculate(s: str) -> int:
    """
    实现基本计算器 II，解析并计算给定字符串表达式的结果。
    
    Args:
    - s: str, 输入的表达式字符串，包含数字、加减乘除运算符和空格。
    
    Returns:
    - int, 表达式的计算结果。
    
    示例:
    >>> calculate("3+2*2")
    7
    >>> calculate(" 3/2 ")
    1
    >>> calculate(" 3+5 / 2 ")
    5
    """
    stack: List[int] = []  # 用于存储中间结果的栈
    num = 0  # 当前解析到的数字
    sign = '+'  # 当前运算符，初始默认为 '+'
    s += '+'  # 在末尾添加一个运算符以处理最后一个数字
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)  # 解析数字
        elif char in '+-*/' or char == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                # 注意：Python中的除法是向零取整的，而题目要求向下取整
                # 所以对于负数结果需要特殊处理
                top = stack.pop()
                if top < 0:
                    stack.append(-(-top // num))
                else:
                    stack.append(top // num)
            num = 0  # 重置num
            sign = char  # 更新运算符
    
    return sum(stack)  # 将栈中所有数求和得到结果

# 测试代码
test_cases = ["3+2*2", " 3/2 ", " 3+5 / 2 "]
results = [calculate(tc) for tc in test_cases]
print(results)  # [7, 1, 5]