from typing import List

def trailing_zeroes(n: int) -> int:
    """
    计算 n! 结果尾数中零的数量。

    参数:
        n (int): 非负整数，表示阶乘的上限。
    
    返回:
        int: n! 结果尾数中零的数量。

    示例:
        >>> trailing_zeroes(5)
        1
        >>> trailing_zeroes(25)
        6
    """
    # 初始化零的数量为 0
    zeros_count = 0
    # 当 n >= 5 时，阶乘结果才可能出现尾数中的零
    while n >= 5:
        # 计算 n 中包含多少个 5 的因子
        n //= 5
        # 累加这些因子到总数
        zeros_count += n
    # 返回尾数中零的总数
    return zeros_count

# 测试代码
test_cases = [3, 5, 10, 25]
results = [trailing_zeroes(n) for n in test_cases]
results
