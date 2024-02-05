def int_to_roman(num: int) -> str:
    """
    将整数转换为罗马数字。

    Args:
    num (int): 需要转换的整数，范围在1到3999之间。

    Returns:
    str: 转换后的罗马数字字符串。

    Examples:
        >>> int_to_roman(3)
        'III'
        >>> int_to_roman(4)
        'IV'
        >>> int_to_roman(9)
        'IX'
        >>> int_to_roman(58)
        'LVIII'
        >>> int_to_roman(1994)
        'MCMXCIV'
    """
    # 映射表，包括特殊的罗马数字表示
    val_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman = []  # 存储结果的罗马数字字符串

    # 遍历映射表，从最大的数值开始匹配
    for value, symbol in val_map:
        # 计算当前数字包含多少个对应的罗马数字
        count, num = divmod(num, value)
        roman.append(symbol * count)  # 将对应的罗马数字加入结果列表

    return ''.join(roman)  # 返回结果字符串

# 测试函数
test_cases = [3, 4, 9, 58, 1994, 3998]
results = [int_to_roman(num) for num in test_cases]
print(results)