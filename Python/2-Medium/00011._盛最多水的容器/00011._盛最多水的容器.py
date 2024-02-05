from typing import List
def max_area(height: List[int]) -> int:
    """
    计算可以盛放最多水的容器的面积。

    Args:
    height: 一个整数列表，表示每个位置的高度。

    Returns:
    int: 最大的水容量。

    示例:
    >>> max_area([1,8,6,2,5,4,8,3,7])
    49
    """
    # 初始化左右指针和最大面积
    left, right, max_area = 0, len(height) - 1, 0

    # 当左指针小于右指针时，执行循环
    while left < right:
        # 计算当前左右指针构成的容器面积
        current_area = min(height[left], height[right]) * (right - left)
        # 更新最大面积
        max_area = max(max_area, current_area)

        # 移动较短边的指针
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# 运行示例
example_height = [1,8,6,2,5,4,8,3,7]
print(f"最大水容量: {max_area(example_height)}")