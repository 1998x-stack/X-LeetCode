from typing import Dict

def fraction_to_decimal(numerator: int, denominator: int) -> str:
    """
    将分数转换为小数字符串，如果存在循环小数，则将循环部分用括号括起来。
    
    Args:
    - numerator (int): 分子
    - denominator (int): 分母
    
    Returns:
    - str: 分数的小数表示
    
    示例:
    >>> fraction_to_decimal(1, 2)
    '0.5'
    >>> fraction_to_decimal(2, 3)
    '0.(6)'
    >>> fraction_to_decimal(4, 333)
    '0.(012)'
    """
    # 处理结果的正负号
    if numerator * denominator < 0:
        sign = "-"
    else:
        sign = ""
    
    # 使用绝对值确保后续计算过程中只处理正数
    numerator, denominator = abs(numerator), abs(denominator)
    
    # 计算整数部分和初始化小数部分
    integer_part, remainder = divmod(numerator, denominator)
    decimal_part = ""
    
    # 用于记录每个余数出现的位置
    remainder_positions: Dict[int, int] = {}
    position = 0  # 小数部分的当前位置
    
    # 处理小数部分，直到余数为0或找到循环开始的位置
    while remainder != 0 and remainder not in remainder_positions:
        remainder_positions[remainder] = position
        remainder *= 10
        digit, remainder = divmod(remainder, denominator)
        decimal_part += str(digit)
        position += 1
    
    # 如果余数为0，没有循环小数
    if remainder == 0:
        if decimal_part:
            return f"{sign}{integer_part}.{decimal_part}"
        else:
            return f"{sign}{integer_part}"
    else:
        # 找到循环开始的位置，并在循环部分前后加上括号
        loop_start = remainder_positions[remainder]
        non_repeating = decimal_part[:loop_start]
        repeating = decimal_part[loop_start:]
        return f"{sign}{integer_part}.{non_repeating}({repeating})"

# 测试代码
test_cases = [
    (1, 2),
    (2, 3),
    (4, 333),
    (-1, -2147483648),
]

# 执行测试并打印结果
for numerator, denominator in test_cases:
    print(f"{numerator}/{denominator} -> {fraction_to_decimal(numerator, denominator)}")