from typing import Dict

def integer_replacement(n: int, memo: Dict[int, int] = {}) -> int:
    """
    使用递归和备忘录的方式，找到将整数n减少到1所需的最小步骤数。
    
    Args:
    n: 待处理的正整数。
    memo: 用于存储已计算结果的备忘录字典。
    
    Returns:
    int: 从n到1所需的最小操作次数。
    
    Examples:
    >>> integer_replacement(8)
    3
    >>> integer_replacement(7)
    4
    """
    # 基础情况：当n为1时，直接返回0
    if n == 1:
        return 0
    # 如果已经计算过这个数，直接从备忘录返回结果
    if n in memo:
        return memo[n]
    
    # 偶数的情况：直接除以2，然后递归调用
    if n % 2 == 0:
        memo[n] = 1 + integer_replacement(n // 2, memo)
    else:
        # 奇数的情况：选择加1或减1中的最小操作次数
        memo[n] = 1 + min(integer_replacement(n + 1, memo), integer_replacement(n - 1, memo))
    
    return memo[n]

# 测试代码
test_cases = [8, 7, 3]
results = {n: integer_replacement(n) for n in test_cases}
print(results)