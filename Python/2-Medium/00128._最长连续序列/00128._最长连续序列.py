from typing import List

def longest_consecutive(nums: List[int]) -> int:
    """
    寻找最长连续序列的长度。
    
    Args:
    nums: List[int] - 一个整数数组
    
    Returns:
    int - 数组中数字连续序列的最长长度
    
    示例:
    >>> longest_consecutive([100, 4, 200, 1, 3, 2])
    4
    """
    # 使用集合去重并提高查找效率
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # 如果当前数字的前一个数字不在集合中，说明可以从当前数字开始尝试构建连续序列
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # 向当前数字的右侧查找连续的数字
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
                
            # 更新最长连续序列的长度
            max_length = max(max_length, current_length)
    
    return max_length

# 测试代码
test_nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(test_nums))