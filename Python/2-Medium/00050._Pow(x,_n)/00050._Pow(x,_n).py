def quick_pow(x: float, n: int) -> float:
    """
    快速幂算法实现计算 x 的 n 次幂。
    
    参数:
    x -- 底数
    n -- 指数
    
    返回:
    x 的 n 次幂
    
    示例:
    >>> quick_pow(2.00000, 10)
    1024.00000
    >>> quick_pow(2.10000, 3)
    9.26100
    >>> quick_pow(2.00000, -2)
    0.25000
    """
    
    # 处理 n 为负数的情况
    if n < 0:
        x = 1 / x
        n = -n
    
    # 初始化结果为 1
    result = 1.0
    
    # 快速幂算法
    while n:
        # 如果 n 为奇数，则将结果乘以 x
        if n % 2 == 1:
            result *= x
        # x 自乘准备下一轮乘法
        x *= x
        # n 右移一位
        n //= 2
    
    return result

# 运行示例测试
test_cases = [
    (2.00000, 10),
    (2.10000, 3),
    (2.00000, -2)
]

# 打印测试结果
for x, n in test_cases:
    print(f"quick_pow({x}, {n}) = {quick_pow(x, n)}")