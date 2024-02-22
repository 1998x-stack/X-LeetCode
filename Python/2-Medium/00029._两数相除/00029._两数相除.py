def divide(dividend: int, divisor: int) -> int:
    """
    实现两数相除，得到商的整数部分。不使用乘法、除法和 mod 运算符。
    
    参数:
    dividend (int): 被除数
    divisor (int): 除数
    
    返回:
    int: 商的整数部分
    
    示例:
    >>> divide(10, 3)
    3
    >>> divide(7, -3)
    -2
    """
    
    # 符号位处理，异号时结果为负
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    
    # 转换为正数处理，避免溢出
    dividend, divisor = abs(dividend), abs(divisor)
    
    # 边界情况处理
    if dividend < divisor:
        return 0
    if divisor == 1:
        result = dividend if sign > 0 else -dividend
        # 检查是否溢出
        return min(max(-2**31, result), 2**31 - 1)
    
    # 初始化商的值
    quotient = 0
    
    # 逐步减去divisor的倍数，直到dividend小于divisor
    while dividend >= divisor:
        # divisor的当前倍数，和相应的指数
        temp, multiple = divisor, 1
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        
        # 减去divisor的倍数，并增加到商中
        dividend -= temp
        quotient += multiple
    
    # 应用符号位
    return quotient if sign == 1 else -quotient

# 测试代码正确性
print(divide(10, 3))  # 应输出3
print(divide(7, -3))  # 应输出-2
print(divide(1, 1))  # 应输出1
print(divide(-2147483648, -1))  # 溢出情况，应输出2147483647