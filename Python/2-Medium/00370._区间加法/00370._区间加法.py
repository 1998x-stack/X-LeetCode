from typing import List

def get_modified_array(length: int, updates: List[List[int]]) -> List[int]:
    """
    应用一系列区间加法操作到一个初始全为0的数组，并返回最终的数组。

    Args:
    - length: int, 数组的长度。
    - updates: List[List[int]], 一系列操作，每个操作是形如 [startIdx, endIdx, inc] 的列表。

    Returns:
    - List[int]: 执行所有操作后的数组。
    
    示例:
    >>> get_modified_array(5, [[1,3,2], [2,4,3], [0,2,-2]])
    [-2, 0, 3, 5, 3]
    """
    # 初始化差分数组
    diff = [0] * length
    
    # 应用每个操作到差分数组
    for start, end, inc in updates:
        diff[start] += inc
        if end + 1 < length:
            diff[end + 1] -= inc
    
    # 通过差分数组构建最终的结果数组
    result = [0] * length
    result[0] = diff[0]
    for i in range(1, length):
        result[i] = result[i-1] + diff[i]
    
    return result

# 测试代码
test_length = 5
test_updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
result_array = get_modified_array(test_length, test_updates)
print(result_array)