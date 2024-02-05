def length_of_longest_substring(s: str) -> int:
    """
    寻找给定字符串中不含重复字符的最长子串长度。

    参数:
        s (str): 输入的字符串

    返回:
        int: 最长子串的长度

    示例:
        >>> length_of_longest_substring("abcabcbb")
        3
        >>> length_of_longest_substring("bbbbb")
        1
    """
    # 初始化指针和哈希表
    start, max_length = 0, 0
    char_index_map = {}

    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            # 更新start指针，防止向回移动
            start = char_index_map[s[end]] + 1
        # 更新字符位置和最大长度
        char_index_map[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# 运行代码并打印重要信息
test_strings = ["abcabcbb", "bbbbb", "", "b", "pwwkew"]
results = {test: length_of_longest_substring(test) for test in test_strings}
print(results)