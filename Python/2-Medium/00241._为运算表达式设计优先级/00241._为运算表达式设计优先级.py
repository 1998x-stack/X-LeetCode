from typing import List

def diffWaysToCompute(input: str) -> List[int]:
    """
    为运算表达式设计优先级，找出所有可能的结果。
    
    参数:
        input (str): 输入的运算表达式。
        
    返回:
        List[int]: 所有可能的运算结果。
        
    方法:
        使用分治策略，递归处理表达式的每个运算符。
    """
    
    # 判断是否为纯数字，如果是，直接返回该数字作为结果的列表
    if input.isdigit():
        return [int(input)]
    
    results = []
    # 遍历表达式的每个字符
    for i, char in enumerate(input):
        # 当前字符如果是运算符
        if char in "+-*":
            # 分治：分别计算左右两部分的所有可能结果
            left = diffWaysToCompute(input[:i])
            right = diffWaysToCompute(input[i+1:])
            
            # 合并结果：根据当前运算符合并左右两部分的结果
            for l in left:
                for r in right:
                    if char == '+':
                        results.append(l + r)
                    elif char == '-':
                        results.append(l - r)
                    else: # char == '*'
                        results.append(l * r)
                        
    return results

# 测试代码
expressions = ["2-1-1", "2*3-4*5"]
for expr in expressions:
    print(f"表达式 '{expr}' 的所有可能结果: {diffWaysToCompute(expr)}")