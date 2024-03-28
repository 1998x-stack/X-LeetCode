from typing import Tuple

def find_n_digit(n: int) -> int:
    """
    寻找无限整数序列中的第 n 位数字。
    
    Args:
    n: 整数，表示要找的位置。
    
    Returns:
    int: 第 n 位的数字。
    
    Examples:
    >>> find_n_digit(3)
    3
    >>> find_n_digit(11)
    0
    """
    # 初始化长度为 1 的数字的数量和这些数字总共占的位数
    length = 1  # 数字的长度
    count = 9  # 长度为 length 的数字总共有多少个
    start = 1  # 当前长度数字的起始值
    
    # 确定 n 所在数字的长度
    while n > length * count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10
    
    # 确定 n 所在的数字
    start += (n - 1) // length  # 找到具体的数字
    # 找到 n 是这个数字中的哪一位，并返回
    return int(str(start)[(n - 1) % length])

# 测试代码
test_cases = [3, 11, 1000]
results = [find_n_digit(n) for n in test_cases]
print(results)