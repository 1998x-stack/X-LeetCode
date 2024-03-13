from typing import List
import math

def maximumGap(nums: List[int]) -> int:
    """
    根据 LeetCode 164题 “最大间距” 实现的解决方案。
    
    Args:
        nums (List[int]): 输入的整数数组。
        
    Returns:
        int: 排序后相邻元素的最大差值。
        
    说明:
        使用桶排序的思想来实现线性时间和空间复杂度的要求。
    """
    if len(nums) < 2:
        return 0
    
    # 计算最大值和最小值
    min_val, max_val = min(nums), max(nums)
    
    # 特殊情况：所有元素相同
    if min_val == max_val:
        return 0
    
    # 确定桶的大小和数量
    bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[None, None] for _ in range(bucket_count)]
    
    # 将元素分配到各个桶中
    for num in nums:
        bucket_idx = (num - min_val) // bucket_size
        if buckets[bucket_idx][0] is None:
            buckets[bucket_idx][0] = num
            buckets[bucket_idx][1] = num
        else:
            buckets[bucket_idx][0] = min(buckets[bucket_idx][0], num)
            buckets[bucket_idx][1] = max(buckets[bucket_idx][1], num)
    
    # 计算最大间距
    max_gap = 0
    previous_max = min_val
    for bucket in buckets:
        if bucket[0] is None:
            continue
        max_gap = max(max_gap, bucket[0] - previous_max)
        previous_max = bucket[1]
    
    return max_gap

# 测试代码
test_nums = [3, 6, 9, 1]
print(maximumGap(test_nums))