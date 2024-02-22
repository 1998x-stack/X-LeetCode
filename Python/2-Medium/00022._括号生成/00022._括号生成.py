from typing import List

def generate_parenthesis(n: int) -> List[str]:
    """
    生成所有可能的且有效的括号组合。
    
    Args:
    n: 括号对数
    
    Returns:
    一个包含所有有效括号组合的列表。
    
    示例:
    >>> generate_parenthesis(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']
    """
    # 结果列表
    res = []
    
    # 回溯函数
    def backtrack(s: str, left: int, right: int):
        """
        使用回溯法生成括号组合。

        Args:
        s: 当前括号字符串
        left: 左括号数量
        right: 右括号数量
        """
        # 如果左括号和右括号数量都达到n，将当前组合添加到结果列表中
        if len(s) == 2 * n:
            res.append(s)
            return
        
        # 如果左括号数量小于n，可以添加一个左括号
        if left < n:
            backtrack(s + '(', left + 1, right)
        
        # 如果右括号数量小于左括号数量，可以添加一个右括号
        if right < left:
            backtrack(s + ')', left, right + 1)
    
    # 从空字符串开始生成括号组合
    backtrack('', 0, 0)
    return res

# 测试函数
print(generate_parenthesis(3))