def reverse_integer(x: int) -> int:
    """
    反转一个32位有符号整数。如果反转后整数溢出，则返回0。
    
    参数:
        x (int): 需要反转的整数。
        
    返回:
        int: 反转后的整数，如果溢出则返回0。
        
    示例:
        >>> reverse_integer(123)
        321
        >>> reverse_integer(-123)
        -321
        >>> reverse_integer(120)
        21
    """
    # 检查是否溢出的辅助函数
    def is_overflow(val):
        return val > 2**31 - 1 or val < -2**31
    
    # 保留符号并将x转换为正数
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    reversed_int = 0
    while x != 0:
        # 提取x的最后一位数字，并更新x
        digit = x % 10
        x //= 10
        
        # 将提取的数字加到reversed_int的末尾
        new_reversed_int = reversed_int * 10 + digit
        # 检查是否溢出
        if is_overflow(new_reversed_int):
            return 0  # 如果溢出，返回0
        
        reversed_int = new_reversed_int
    
    # 根据原始数的符号返回结果
    return sign * reversed_int

# 测试用例
test_cases = [123, -123, 120, 0, 1534236469]

# 运行测试用例
results = {case: reverse_integer(case) for case in test_cases}
print(results)
