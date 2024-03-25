from typing import List

def max_subarray_length_equal_k(nums: List[int], k: int) -> int:
    """
    寻找和为 k 的最长子数组长度

    Args:
    nums: List[int], 给定的整数数组
    k: int, 目标和

    Returns:
    int: 和为 k 的最长子数组长度

    示例:
    >>> max_subarray_length_equal_k([1, -1, 5, -2, 3], 3)
    4
    """
    # 初始化前缀和哈希表，键为前缀和，值为该前缀和最早出现的索引
    prefix_sum_index = {0: -1}  # 处理从头开始累加等于 k 的情况
    max_length = 0  # 初始化最长子数组长度
    current_sum = 0  # 初始化当前前缀和

    # 遍历数组，计算前缀和
    for i, num in enumerate(nums):
        current_sum += num
        # 如果 current_sum - k 存在于哈希表中，更新 max_length
        if current_sum - k in prefix_sum_index:
            max_length = max(max_length, i - prefix_sum_index[current_sum - k])
        # 如果当前前缀和不在哈希表中，则添加它
        if current_sum not in prefix_sum_index:
            prefix_sum_index[current_sum] = i

    return max_length

# 测试函数
print(max_subarray_length_equal_k([1, -1, 5, -2, 3], 3))  # 应输出 4