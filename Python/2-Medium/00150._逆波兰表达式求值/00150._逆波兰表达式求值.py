from typing import List

def evaluate_reverse_polish_notation(tokens: List[str]) -> int:
    """
    计算逆波兰表达式的值。
    
    Args:
        tokens: 一个字符串列表，代表逆波兰表达式。
    
    Returns:
        表达式的计算结果。
    
    示例:
        >>> evaluate_reverse_polish_notation(["2", "1", "+", "3", "*"])
        9
        >>> evaluate_reverse_polish_notation(["4", "13", "5", "/", "+"])
        6
    """
    stack = []  # 初始化栈
    # 遍历每个元素
    for token in tokens:
        if token in "+-*/":  # 如果元素是运算符
            # 从栈中弹出两个元素作为操作数
            num2 = stack.pop()
            num1 = stack.pop()
            # 根据运算符进行计算，并将结果压回栈中
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            else:  # 处理除法，注意向零取整
                stack.append(int(num1 / num2))
        else:  # 如果元素是数字，将其转换为整数后压入栈中
            stack.append(int(token))
    
    return stack[0]  # 遍历完成后，栈顶元素即为结果

# 运行示例
example_1 = ["2", "1", "+", "3", "*"]
example_2 = ["4", "13", "5", "/", "+"]
print(evaluate_reverse_polish_notation(example_1))  # 应输出 9
print(evaluate_reverse_polish_notation(example_2))  # 应输出 6