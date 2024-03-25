from typing import List

def isValidSerialization(preorder: str) -> bool:
    """
    验证给定的前序序列化是否正确
    
    Args:
    - preorder: str, 一个表示二叉树前序遍历的序列化字符串
    
    Returns:
    - bool, 序列化是否有效
    
    """
    # 将输入的序列化字符串按逗号分割
    nodes = preorder.split(',')
    stack = []  # 初始化栈
    for node in nodes:
        while node == "#" and stack and stack[-1] == "#":
            stack.pop()  # 弹出栈顶的“#”
            if not stack:
                return False  # 如果没有非“#”节点可以弹出，序列无效
            stack.pop()  # 弹出对应的非“#”节点
        stack.append(node)  # 将当前节点推入栈中
    
    # 如果有效，最终栈中应只剩下一个“#”
    return len(stack) == 1 and stack[0] == "#"

# 测试代码
test_cases = [
    "9,3,4,#,#,1,#,#,2,#,6,#,#",  # True
    "1,#",                        # False
    "9,#,#,1",                    # False
    "1",                          # True
]

# 执行测试
results = [isValidSerialization(case) for case in test_cases]
print(results)