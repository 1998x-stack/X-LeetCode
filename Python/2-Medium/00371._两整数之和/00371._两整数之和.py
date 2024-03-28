from typing import Tuple

def sum_of_two_integers(a: int, b: int) -> int:
    """
    使用位运算实现两整数之和。

    参数:
    a (int): 整数a。
    b (int): 整数b。

    返回:
    int: a和b的和。

    示例:
    >>> sum_of_two_integers(1, 2)
    3
    >>> sum_of_two_integers(-2, 3)
    1
    """
    # 32位整数的最大值
    MAX = 0x7FFFFFFF
    # 32位整数的掩码（用于处理Python中整数的无限精度特性）
    mask = 0xFFFFFFFF
    
    while b != 0:
        # 计算无进位和，同时应用掩码限制结果为32位
        sum_without_carry = (a ^ b) & mask
        # 计算进位，同时应用掩码限制结果为32位，并左移一位准备下一次迭代
        carry = ((a & b) << 1) & mask
        
        # 更新a和b为下一次迭代准备
        a, b = sum_without_carry, carry
    
    # 如果结果为负数，进行转换
    return a if a <= MAX else ~(a ^ mask)

# 测试代码
test_cases = [
    (1, 2),  # 示例1: 正数加法
    (-2, 3),  # 示例2: 负数和正数加法
    (-1, -1),  # 示例3: 负数加法
]

# 执行测试用例
results = [(a, b, sum_of_two_integers(a, b)) for a, b in test_cases]

# 打印结果
for a, b, result in results:
    print(f"{a} + {b} = {result}")