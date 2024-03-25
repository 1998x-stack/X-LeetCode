from typing import Dict, Set

def remove_duplicate_letters(s: str) -> str:
    """
    去除字符串中的重复字母，确保每个字母只出现一次且结果的字典序最小。
    
    参数:
        s (str): 输入的字符串。
        
    返回:
        str: 去除重复字母后，字典序最小的字符串。
    
    示例:
        >>> remove_duplicate_letters("bcabc")
        'abc'
        >>> remove_duplicate_letters("cbacdcbc")
        'acdb'
    """
    # 记录每个字符出现的次数
    char_count: Dict[str, int] = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # 使用栈来保存最终的字符串，保证字典序最小
    stack: list = []
    # 记录栈中已有的字符，避免重复加入
    in_stack: Set[str] = set()
    
    # 遍历字符串
    for char in s:
        # 当前字符如果未在栈中，则尝试加入栈
        if char not in in_stack:
            # 当栈不为空且当前字符字典序小于栈顶字符，且栈顶字符在后续还会出现时，弹出栈顶字符
            while stack and char < stack[-1] and char_count[stack[-1]] > 0:
                in_stack.remove(stack.pop())
            # 当前字符压栈，并标记为已入栈
            stack.append(char)
            in_stack.add(char)
        
        # 无论是否加入栈，当前字符的计数都应减1
        char_count[char] -= 1
    
    # 将栈中的字符合并成最终字符串
    return ''.join(stack)

# 运行代码示例
print(remove_duplicate_letters("bcabc"))  # 期望输出: "abc"
print(remove_duplicate_letters("cbacdcbc"))  # 期望输出: "acdb"
