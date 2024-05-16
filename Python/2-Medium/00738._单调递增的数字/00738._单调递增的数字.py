from typing import List

def monotone_increasing_digits(N: int) -> int:
    """
    找到小于或等于N的最大单调递增的数字。
    
    参数:
        N: 一个非负整数
    
    返回:
        小于或等于N的最大单调递增的数字
    
    示例:
        >>> monotone_increasing_digits(332)
        299
    """
    # 将N转换为字符串以便逐位处理
    digits = list(str(N))
    length = len(digits)
    mark = length
    
    # 从后往前遍历，找到第一个递减的位置
    for i in range(length - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            mark = i
            digits[i - 1] = str(int(digits[i - 1]) - 1)
    
    # 将mark后的所有数字置为9
    for i in range(mark, length):
        digits[i] = '9'
    
    return int(''.join(digits))

# 验证几个测试样例
test_1 = monotone_increasing_digits(10)
test_2 = monotone_increasing_digits(1234)
test_3 = monotone_increasing_digits(332)
print(test_1, test_2, test_3)