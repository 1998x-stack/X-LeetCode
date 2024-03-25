from typing import List

def is_additive_number(num: str) -> bool:
    """
    判断给定的字符串是否为累加数。

    Args:
    num: 字符串，代表一个可能的累加数序列。

    Returns:
    bool: 如果字符串是累加数，则返回True；否则返回False。
    """

    def add_str(num1: str, num2: str) -> str:
        """字符串表示的两个数相加"""
        # 翻转字符串，便于从最低位开始加法运算
        num1, num2 = num1[::-1], num2[::-1]
        carry, result = 0, []
        for i in range(max(len(num1), len(num2))):
            n1 = int(num1[i]) if i < len(num1) else 0
            n2 = int(num2[i]) if i < len(num2) else 0
            sum_val = n1 + n2 + carry
            carry = sum_val // 10
            result.append(str(sum_val % 10))
        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])

    def valid_additive_sequence(start: int, num1: str, num2: str) -> bool:
        """递归验证后续字符串是否能构成累加数列"""
        if start == len(num):
            return True
        sum_str = add_str(num1, num2)
        sum_len = len(sum_str)
        if start + sum_len <= len(num) and num[start:start+sum_len] == sum_str:
            return valid_additive_sequence(start + sum_len, num2, sum_str)
        return False

    # 主函数逻辑
    n = len(num)
    for i in range(1, n):
        for j in range(i+1, n):
            num1, num2 = num[:i], num[i:j]
            # 如果num1或num2以'0'开头且长度大于1，直接跳过
            if (num1.startswith('0') and len(num1) > 1) or (num2.startswith('0') and len(num2) > 1):
                continue
            if valid_additive_sequence(j, num1, num2):
                return True
    return False

# 测试示例
print(is_additive_number("112358"))  # 应返回 True
print(is_additive_number("199100199"))  # 应返回 True
