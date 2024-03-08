from typing import List

def can_split(nums: List[int]) -> bool:
    """
    检查是否可以将数组分割成和相等的四个子数组

    Args:
    nums: List[int] - 输入的整数数组

    Returns:
    bool - 是否可以分割成和相等的四个子数组

    示例:
    >>> can_split([1,2,1,2,1,2,1])
    True
    """
    n = len(nums)
    if n < 6:  # 数组长度小于6，无法分割成四部分
        return False

    # 计算前缀和
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    # 使用哈希表存储中间两部分和相等的情况
    for j in range(3, n - 2):
        sum_set = set()
        for i in range(1, j - 1):
            if prefix_sum[i] == prefix_sum[j] - prefix_sum[i + 1]:
                sum_set.add(prefix_sum[i])
        for k in range(j + 2, n - 1):
            if prefix_sum[n] - prefix_sum[k + 1] == prefix_sum[k] - prefix_sum[j + 1] and (prefix_sum[k] - prefix_sum[j + 1]) in sum_set:
                return True
    return False

# 测试代码
test_nums = [1,2,1,2,1,2,1]
can_split(test_nums)