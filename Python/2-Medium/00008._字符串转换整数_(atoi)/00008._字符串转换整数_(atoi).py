def myAtoi(s: str) -> int:
    """
    字符串转换为整数 (atoi) 实现。

    Args:
        s (str): 输入的字符串。

    Returns:
        int: 转换后的整数。

    示例:
        >>> myAtoi("42")
        42
        >>> myAtoi("   -42")
        -42
        >>> myAtoi("4193 with words")
        4193
    """
    i = 0
    n = len(s)
    # 去除前导空格
    while i < n and s[i] == ' ':
        i += 1

    # 处理空字符串或只有空格的情况
    if i == n:
        return 0

    # 检测正负号
    sign = 1
    if s[i] == '+' or s[i] == '-':
        sign = -1 if s[i] == '-' else 1
        i += 1

    result = 0
    max_int, min_int = 2**31 - 1, -2**31
    while i < n and s[i].isdigit():
        digit = int(s[i])
        # 检查溢出
        if result > max_int // 10 or (result == max_int // 10 and digit > max_int % 10):
            return max_int if sign == 1 else min_int
        
        result = result * 10 + digit
        i += 1

    return result * sign

# 测试函数
if __name__ == "__main__":
    test_cases = ["42", "   -42", "4193 with words", "", " "]
    for test in test_cases:
        print(f"{test!r}: {myAtoi(test)}")
