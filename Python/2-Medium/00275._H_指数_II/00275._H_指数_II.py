from typing import List

def h_index(citations: List[int]) -> int:
    """
    使用二分查找算法计算 H 指数。

    Args:
    citations (List[int]): 已排序的引用次数数组。

    Returns:
    int: 研究者的 H 指数。
    """
    left, right = 0, len(citations) - 1
    while left <= right:
        mid = (left + right) // 2
        # 检查是否满足 H 指数的条件
        if citations[mid] < len(citations) - mid:
            left = mid + 1  # 向右搜索
        else:
            right = mid - 1  # 向左搜索
    # 计算 H 指数
    return len(citations) - left

# 示例运行
citations = [0, 1, 3, 5, 6, 7]
h_index_result = h_index(citations)
print(h_index_result)  # 3