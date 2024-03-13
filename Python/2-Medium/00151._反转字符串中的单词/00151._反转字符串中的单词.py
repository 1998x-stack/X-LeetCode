from typing import List

def remove_extra_spaces(s: str) -> str:
    """
    去除字符串中的多余空格，保留单词间一个空格，移除首尾空格。
    
    参数:
        s (str): 输入的字符串。
        
    返回:
        str: 处理后的字符串。
    """
    left, right = 0, len(s) - 1
    # 去除字符串开头的空格
    while left <= right and s[left] == ' ':
        left += 1
    # 去除字符串结尾的空格
    while left <= right and s[right] == ' ':
        right -= 1

    # 去除单词间多余的空格
    result = []
    while left <= right:
        if s[left] != ' ':
            result.append(s[left])
        elif result[-1] != ' ':  # 当前字符是空格，但结果中最后一个字符不是空格时添加
            result.append(s[left])
        left += 1
    return ''.join(result)

def reverse_string(s: List[str], left: int, right: int) -> None:
    """
    反转字符串指定区间内的字符。
    
    参数:
        s (List[str]): 字符列表。
        left (int): 反转区间的左边界。
        right (int): 反转区间的右边界。
    """
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1

def reverse_words(s: str) -> str:
    """
    反转字符串中的单词。
    
    参数:
        s (str): 输入的字符串。
        
    返回:
        str: 单词顺序反转后的字符串。
    """
    # 去除多余空格
    s = remove_extra_spaces(s)
    s_list = list(s)
    # 反转整个字符串
    reverse_string(s_list, 0, len(s_list) - 1)
    
    # 反转每个单词
    start = end = 0
    while start < len(s_list):
        while end < len(s_list) and s_list[end] != ' ':
            end += 1
        reverse_string(s_list, start, end - 1)
        start = end + 1
        end += 1
    
    return ''.join(s_list)

# 测试代码
test_str = "  the sky is  blue  "
print(reverse_words(test_str))  # 输出 "blue is sky the"