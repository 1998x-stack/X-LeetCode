from typing import List

def generate_palindromes(n: str) -> List[str]:
    """
    生成与n长度相同，且可能作为最近回文数的候选。

    参数:
    n: 输入的字符串表示的数值。

    返回:
    一个包含可能的回文数候选的列表。
    """
    length = len(n)
    candidates = []
    # 基于n的前半部分生成回文数
    half = int(n[:(length + 1) // 2])
    for diff in (-1, 0, 1):
        # 构造前半部分，然后根据长度是奇数还是偶数来生成完整的回文数
        new_half = str(half + diff)
        if length % 2 == 0:
            candidate = new_half + new_half[::-1]
        else:
            candidate = new_half + new_half[:-1][::-1]
        candidates.append(candidate)
    # 添加特殊情况，考虑极小值和极大值附近的回文数
    candidates.append("1" + "0" * (length - 1) + "1")  # 如1001
    candidates.append("9" * (length - 1))  # 如999
    return candidates

def find_closest_palindrome(n: str) -> str:
    """
    找到与给定数字n最接近的回文数。

    参数:
    n: 输入的字符串表示的数值。

    返回:
    最接近的回文数的字符串表示。
    """
    # 如果n为1，则直接返回0
    if n == "1":
        return "0"
    
    candidates = generate_palindromes(n)
    min_distance = float('inf')
    result = None
    for candidate in candidates:
        # 排除自身，只考虑其他回文数
        if candidate != n:
            distance = abs(int(candidate) - int(n))
            if distance < min_distance or (distance == min_distance and int(candidate) < int(result)):
                min_distance = distance
                result = candidate
    
    return result

# 测试代码
test_n = "123"
result = find_closest_palindrome(test_n)
print(f"与'{test_n}'最近的回文数是: {result}")