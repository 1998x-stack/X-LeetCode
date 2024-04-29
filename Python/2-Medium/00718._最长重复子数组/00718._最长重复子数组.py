from typing import List

def find_length(nums1: List[int], nums2: List[int]) -> int:
    """
    计算两个数组的最长重复子数组的长度。
    
    Args:
    nums1 (List[int]): 第一个整数数组。
    nums2 (List[int]): 第二个整数数组。
    
    Returns:
    int: 最长重复子数组的长度。
    
    Examples:
    >>> find_length([1,2,3,2,1], [3,2,1,4,7])
    3
    """
    m, n = len(nums1), len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    for i in range(m):
        for j in range(n):
            if nums1[i] == nums2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                max_length = max(max_length, dp[i + 1][j + 1])
            else:
                dp[i+1][j+1] = 0
                
    return max_length


# 测试代码
test_nums1 = [1, 2, 3, 2, 1]
test_nums2 = [3, 2, 1, 4, 7]
result = find_length(test_nums1, test_nums2)
print(f"最长重复子数组的长度为: {result}")