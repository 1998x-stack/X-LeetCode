from typing import List, Dict, Tuple
import heapq

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    找出数组中出现频率前 k 高的元素。

    Args:
    nums: 整数数组。
    k: 需要返回的频率最高的元素数量。

    Returns:
    一个列表，包含出现频率前 k 高的元素。

    """
    # 使用哈希表统计每个元素出现的频率
    frequency_map: Dict[int, int] = {}
    for num in nums:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
            
    # 构建一个最小堆，用于存储频率及对应的元素，元素为(频率, 元素)的元组
    min_heap: List[Tuple[int, int]] = []
    
    # 遍历频率哈希表，使用堆维护频率最高的k个元素
    for num, freq in frequency_map.items():
        # 如果堆的大小小于k，直接添加
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        # 如果当前元素的频率大于堆顶元素的频率，替换堆顶元素
        elif freq > min_heap[0][0]:
            heapq.heappushpop(min_heap, (freq, num))
    
    # 提取堆中的元素，即为频率最高的k个元素
    top_k_elements = [num for freq, num in min_heap]
    return top_k_elements

# 测试代码
nums = [1,1,1,2,2,3]
k = 2
print(top_k_frequent(nums, k))  # [1, 2]