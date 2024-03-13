from typing import Dict

def length_of_longest_substring_two_distinct(s: str) -> int:
    """
    寻找最多包含两个不同字符的最长子串的长度。

    Args:
    s (str): 输入字符串。

    Returns:
    int: 最长子串的长度。

    示例:
    >>> length_of_longest_substring_two_distinct("eceba")
    3
    >>> length_of_longest_substring_two_distinct("ccaabbb")
    5
    """
    # 初始化哈希表，用于记录窗口中每个字符的出现次数
    char_count: Dict[str, int] = {}
    left = 0  # 窗口左边界
    max_len = 0  # 最大子串长度

    # 遍历字符串，使用right作为窗口的右边界
    for right in range(len(s)):
        # 将当前字符加入哈希表，如果字符不存在，则初始化为0再加1
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # 当窗口内不同字符超过2个时，收缩窗口
        while len(char_count) > 2:
            char_count[s[left]] -= 1  # 减少左侧字符的计数
            if char_count[s[left]] == 0:  # 如果某字符计数为0，则从哈希表中移除
                del char_count[s[left]]
            left += 1  # 移动窗口的左边界

        # 更新最大子串长度
        max_len = max(max_len, right - left + 1)

    return max_len

# 测试代码
test_cases = ["eceba", "ccaabbb"]
results = [length_of_longest_substring_two_distinct(case) for case in test_cases]
print(results)  # [3, 5]