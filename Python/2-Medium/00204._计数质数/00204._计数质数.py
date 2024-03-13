from typing import List

def count_primes(n: int) -> int:
    """
    计算小于非负整数 n 的质数的数量。

    Args:
    n: 非负整数，计算小于该数的质数数量。

    Returns:
    质数的数量。

    示例:
    >>> count_primes(10)
    4
    """
    if n <= 2:  # 边界情况处理
        return 0

    is_prime = [True] * n  # 初始化质数标记数组
    is_prime[0] = is_prime[1] = False  # 0 和 1 不是质数

    for i in range(2, int(n ** 0.5) + 1):  # 只需遍历到 sqrt(n)
        if is_prime[i]:
            # 标记 i 的倍数为非质数
            is_prime[i*i:n:i] = [False] * ((n-1-i*i)//i + 1)

    return sum(is_prime)  # 计数并返回质数的数量

# 运行示例
n = 10
print(f"小于 {n} 的质数数量为：", count_primes(n))