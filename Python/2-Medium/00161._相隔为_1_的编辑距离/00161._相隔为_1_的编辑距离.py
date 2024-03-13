from typing import Tuple

def is_one_edit_distance(s: str, t: str) -> bool:
    """
    判断两个字符串是否恰好相差一个编辑距离。
    
    Args:
    s: 第一个字符串。
    t: 第二个字符串。
    
    Returns:
    bool: 如果两个字符串恰好相差一个编辑距离，则为True；否则为False。
    """
    # 计算两个字符串的长度
    len_s, len_t = len(s), len(t)
    
    # 如果长度差大于1，则直接返回False
    if abs(len_s - len_t) > 1:
        return False
    
    # 如果两个字符串长度相同
    if len_s == len_t:
        diff_count = 0  # 记录不同字符的数量
        for char_s, char_t in zip(s, t):
            if char_s != char_t:
                diff_count += 1
                # 如果不同字符超过1个，直接返回False
                if diff_count > 1:
                    return False
        # 最后判断不同字符是否恰好为1
        return diff_count == 1
    
    # 确保s是较短的字符串，如果不是，交换它们
    if len_s > len_t:
        s, t = t, s
    
    # 使用双指针遍历字符串
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            # 如果字符不同，较长字符串的指针前进，较短的保持不变
            # 之后的字符必须完全相同，否则返回False
            return s[i:] == t[j+1:]
        i += 1
        j += 1
    
    # 如果所有字符都检查完毕，说明只有最后一个字符是不同的
    return True

# 测试函数
test_cases = [
    ("ab", "acb"),  # True
    ("cab", "ad"),  # False
    ("1203", "1213"),  # True
]

# 运行测试
for s, t in test_cases:
    result = is_one_edit_distance(s, t)
    print(f"'{s}' and '{t}' -> {result}")
