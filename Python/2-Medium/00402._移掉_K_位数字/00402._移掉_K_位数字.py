from typing import List

def remove_k_digits(num: str, k: int) -> str:
    """
    移除给定数字中的 k 位数字，使得剩余数字最小。
    
    Args:
    num: 字符串形式的非负整数。
    k: 需要移除的数字数量。
    
    Returns:
    一个表示最小数字的字符串。
    
    Examples:
    >>> remove_k_digits("1432219", 3)
    '1219'
    >>> remove_k_digits("10200", 1)
    '200'
    >>> remove_k_digits("10", 2)
    '0'
    """
    # 初始化一个栈，用于存放最终结果的数字
    stack: List[str] = []
    for digit in num:
        # 当栈不为空且还可以移除数字时，如果当前数字小于栈顶元素，则弹出栈顶元素
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # 如果 k 仍大于 0，则从栈顶开始移除，直至 k 减到 0
    while k > 0:
        stack.pop()
        k -= 1
    
    # 将栈中的元素转换为字符串，同时去除前导零
    result = "".join(stack).lstrip('0')
    
    # 如果结果为空字符串，返回 '0'，否则返回结果字符串
    return result if result else '0'

# 运行示例
test_cases = [
    ("1432219", 3),
    ("10200", 1),
    ("10", 2)
]

# 打印测试用例的结果
for num, k in test_cases:
    print(f"remove_k_digits({num}, {k}) = {remove_k_digits(num, k)}")