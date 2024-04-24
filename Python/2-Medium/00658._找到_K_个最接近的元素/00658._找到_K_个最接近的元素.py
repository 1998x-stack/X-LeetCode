from typing import List

def bisect_left(arr: List[int], x: int) -> int:
    """
    实现二分查找的自定义函数，以找到元素 x 应该插入的位置，以保持列表排序。

    参数:
        arr (List[int]): 已排序的整数数组。
        x (int): 要查找插入位置的元素。

    返回:
        int: 插入位置的索引。
    """
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low

def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    """
    在有序数组中找到最接近 x 的 k 个数。
    """
    size = len(arr)
    # 使用自定义的 bisect_left 函数
    left = bisect_left(arr, x) - 1
    right = left + 1

    while right - left - 1 < k:
        if left == -1:
            right += 1
        elif right == size or (x - arr[left] <= arr[right] - x):
            left -= 1
        else:
            right += 1

    return arr[left + 1:right]

# 测试代码
result = find_closest_elements([1, 2, 3, 4, 5], 4, 3)
print(result)  # 应当输出 [1, 2, 3, 4]