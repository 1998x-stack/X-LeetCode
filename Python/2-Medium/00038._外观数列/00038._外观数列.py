def count_and_say(n: int) -> str:
    """
    生成外观数列的第 n 项

    参数:
    n -- 外观数列的项数

    返回:
    外观数列的第 n 项字符串

    示例:
    >>> count_and_say(1)
    '1'
    >>> count_and_say(4)
    '1211'
    """
    # 初始化第一项
    current = "1"
    
    # 对于每一项进行迭代
    for _ in range(1, n):
        next_seq = ""  # 准备下一项
        i = 0  # 段落开始位置
        
        # 遍历当前项
        while i < len(current):
            count = 1  # 计数器
            # 统计相同数字的连续长度
            while i + 1 < len(current) and current[i] == current[i + 1]:
                i += 1
                count += 1
            
            # 构建下一项
            next_seq += str(count) + current[i]
            i += 1
        
        # 准备下一轮迭代
        current = next_seq
    
    # 返回最终结果
    return current

# 测试代码
print(count_and_say(1))  # 应输出: '1'
print(count_and_say(4))  # 应输出: '1211'
print(count_and_say(5))  # 测试更大的n，验证逻辑正确性
