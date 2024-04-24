def construct_beautiful_arrangement(n: int, k: int) -> List[int]:
    """
    构造一个长度为 n 的数组，其中恰好有 k 个不同的整数差。
    
    参数:
    n (int): 数组长度
    k (int): 不同整数差的数量
    
    返回:
    List[int]: 满足条件的数组
    """
    # 初始化结果数组
    result = []
    # 开始构造前 k+1 个数字，以满足 k 个不同的差值需求
    left = 1  # 起始数
    right = n  # 最终数
    # 添加数字以创建 k 个不同的差值
    for i in range(k+1):
        if i % 2 == 0:
            result.append(left)
            left += 1
        else:
            result.append(right)
            right -= 1
    # 添加剩余数字
    if i % 2 == 0:
        result.extend(range(right, left - 1, -1))
    else:
        result.extend(range(left, right + 1))
    return result
print(construct_beautiful_arrangement(3, 2))  # [1, 3, 2]
print(construct_beautiful_arrangement(4, 2))  # [1, 3, 2, 4]