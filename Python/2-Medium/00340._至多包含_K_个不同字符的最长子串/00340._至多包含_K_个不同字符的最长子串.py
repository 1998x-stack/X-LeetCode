from typing import Dict

def longest_substring_with_at_most_k_distinct_characters(s: str, k: int) -> int:
    """
    寻找最多包含 k 个不同字符的最长子串的长度。
    
    参数:
    s: 字符串。
    k: 整数，表示最多不同字符的数量。
    
    返回:
    最长子串的长度。
    
    示例:
    >>> longest_substring_with_at_most_k_distinct_characters("eceba", 2)
    3
    >>> longest_substring_with_at_most_k_distinct_characters("aa", 1)
    2
    """
    
    # 初始化左右指针，最长长度，和字符计数哈希表
    left, right, max_length = 0, 0, 0
    char_count: Dict[str, int] = {}
    
    # 遍历字符串
    while right < len(s):
        # 如果字符在哈希表中，则增加计数；否则，添加到哈希表中
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # 当窗口内不同字符数量超过 k 时，收缩左侧窗口
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # 更新最长子串的长度
        max_length = max(max_length, right - left + 1)
        right += 1
    
    return max_length

# 运行代码并测试
test_cases = [
    ("eceba", 2),  # 示例1
    ("aa", 1),     # 示例2
]

# 执行测试
for s, k in test_cases:
    print(f"字符串: '{s}', k = {k}, 最长子串长度: {longest_substring_with_at_most_k_distinct_characters(s, k)}")