from typing import List, Tuple
import heapq

def k_smallest_pairs(nums1: List[int], nums2: List[int], k: int) -> List[Tuple[int, int]]:
    """
    找到和最小的k对数字。
    
    参数:
    nums1 (List[int]): 第一个列表。
    nums2 (List[int]): 第二个列表。
    k (int): 要找到的对数。
    
    返回:
    List[Tuple[int, int]]: 和最小的k对数字。
    
    示例:
    >>> k_smallest_pairs([1,7,11], [2,4,6], 3)
    [(1, 2), (1, 4), (1, 6)]
    """
    
    # 检查边界条件
    if not nums1 or not nums2 or k <= 0:
        return []
    
    # 初始化优先队列，元素为(数对和，nums1索引，nums2索引)
    heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(len(nums1), k))]
    heapq.heapify(heap)
    
    # 存储结果的列表
    result = []
    
    # 循环提取和最小的对，直到找到k对或优先队列为空
    while heap and k > 0:
        _, i, j = heapq.heappop(heap)
        result.append((nums1[i], nums2[j]))
        k -= 1
        # 如果还有nums2中的元素可以与nums1[i]组成对，则加入新的对
        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
    
    return result

# 测试函数
test_nums1 = [1, 7, 11]
test_nums2 = [2, 4, 6]
test_k = 3
print(k_smallest_pairs(test_nums1, test_nums2, test_k))