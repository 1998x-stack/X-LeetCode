from typing import List, Dict, Tuple, Any

def count_numbers_with_unique_digits(n: int) -> int:
    """
    计算所有位数都是不同的数字的数量。
    
    Args:
    n: 非负整数，表示最大的位数。
    
    Returns:
    int: 所有位数都是不同的数字的数量。
    
    示例:
    >>> count_numbers_with_unique_digits(2)
    91
    """
    if n == 0:
        return 1
    if n > 10:
        n = 10  # 超过10位数字不可能所有位都不同
    total = 10  # 当n=1时，有10种可能（0-9）
    unique_digits = 9  # 第一位数字（不包括0）
    available_numbers = 9  # 可用于后续位的数字数量
    for i in range(2, n + 1):
        unique_digits *= available_numbers
        total += unique_digits
        available_numbers -= 1
    return total

# 运行测试案例
test_cases = [0, 1, 2, 3, 11]
results = {n: count_numbers_with_unique_digits(n) for n in test_cases}
print(results)