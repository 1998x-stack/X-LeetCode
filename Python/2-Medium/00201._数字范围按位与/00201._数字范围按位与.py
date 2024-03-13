from typing import Any

def range_bitwise_and(m: int, n: int) -> int:
    """
    计算在范围 [m, n] 内所有数字的按位与的结果。

    参数:
    m (int): 范围的起始整数。
    n (int): 范围的结束整数。

    返回:
    int: 范围内所有数字按位与的结果。

    示例:
    >>> range_bitwise_and(5, 7)
    4
    >>> range_bitwise_and(0, 1)
    0
    """
    # 初始化偏移量
    shift = 0
    # 当 m 小于 n 时，寻找公共前缀
    while m < n:
        # 右移 m 和 n，去除最低位
        m >>= 1
        n >>= 1
        # 增加偏移量
        shift += 1
    # 将 m 左移 shift 位，还原被移除的位数
    return m << shift

# 运行示例
test_cases = [(5, 7), (0, 1)]
results = [range_bitwise_and(m, n) for m, n in test_cases]
print(results)