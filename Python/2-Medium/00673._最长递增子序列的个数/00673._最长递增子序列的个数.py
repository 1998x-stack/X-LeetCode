from typing import List

def find_number_of_LIS(nums: List[int]) -> int:
    """
    计算给定数组的最长递增子序列的个数。
    
    参数:
        nums (List[int]): 输入的整数数组。
    
    返回:
        int: 最长递增子序列的个数。
    
    示例:
        >>> find_number_of_LIS([1,3,5,4,7])
        2
        >>> find_number_of_LIS([2,2,2,2,2])
        5
    """
    if not nums:
        return 0
    n = len(nums)
    lengths = [1] * n # lengths[i] 是以 nums[i] 结尾的最长递增子序列的长度
    counts = [1] * n # counts[i] 是以 nums[i] 结尾的最长递增子序列的个数
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j]
    
    max_length = max(lengths)
    return sum(count for i, count in enumerate(counts) if lengths[i] == max_length)

# 示例运行
test_cases = [
    [1, 3, 5, 4, 7],
    [2, 2, 2, 2, 2]
]

results = [find_number_of_LIS(case) for case in test_cases]
print(results)