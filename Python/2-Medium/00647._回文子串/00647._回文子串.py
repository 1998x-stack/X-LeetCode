from typing import List

def count_substrings(s: str) -> int:
    """
    计算字符串中的回文子串数量。
    
    参数:
        s (str): 输入的字符串。
    
    返回:
        int: 回文子串的数量。
    
    示例:
        >>> count_substrings("abc")
        3
        >>> count_substrings("aaa")
        6
    """
    def expand_around_center(left, right):
        count = 0
        while left >=0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    palindrome_count = 0
    for i in range(len(s)):
        palindrome_count += expand_around_center(i, i)
        if i + 1 < len(s):
            palindrome_count += expand_around_center(i, i + 1)
    return palindrome_count
    
# 测试代码
s1 = "abc"
s2 = "aaa"
print(f"回文子串数量（输入'{s1}'）：", count_substrings(s1))
print(f"回文子串数量（输入'{s2}'）：", count_substrings(s2))