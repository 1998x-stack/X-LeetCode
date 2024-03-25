from typing import List

def sort_transformed_array(nums: List[int], a: int, b: int, c: int) -> List[int]:
    """
    根据给定的二次函数 a*x^2 + b*x + c，转化有序数组，并返回转化后同样有序的数组。

    Args:
    nums: List[int] - 输入的有序数组。
    a, b, c: int - 二次函数的系数。

    Returns:
    List[int] - 转化后的有序数组。

    说明:
    - 首先分析二次函数的性质（开口向上或向下），以确定填充结果数组的方向。
    - 利用双指针从两端向中间遍历原数组，根据二次函数性质选取适当的值填充到结果数组。
    - 最后，如果二次函数开口向上，反转结果数组以满足升序排列的要求。
    """

    # 定义二次函数转化方法
    def transform(x: int) -> int:
        return a * x ** 2 + b * x + c

    n = len(nums)
    # 初始化结果数组
    result = [0] * n
    # 双指针初始化：left指向起始位置，right指向末尾位置
    left, right = 0, n - 1
    # 根据a的值决定填充结果数组的起始位置
    fill_index = n - 1 if a >= 0 else 0

    while left <= right:
        left_transformed = transform(nums[left])
        right_transformed = transform(nums[right])
        # 如果a大于等于0，二次函数开口向上，选择较大的值从数组末尾开始填充
        if a >= 0:
            if left_transformed > right_transformed:
                result[fill_index] = left_transformed
                left += 1
            else:
                result[fill_index] = right_transformed
                right -= 1
            fill_index -= 1  # 填充位置向左移动
        else:  # 如果a小于0，二次函数开口向下，选择较小的值从数组开头开始填充
            if left_transformed < right_transformed:
                result[fill_index] = left_transformed
                left += 1
            else:
                result[fill_index] = right_transformed
                right -= 1
            fill_index += 1  # 填充位置向右移动

    return result

# 测试代码
# 示例数组和二次函数参数
nums = [-4, -2, 2, 4]
a, b, c = 1, 3, 5
# 调用函数并打印结果
sorted_transformed_array = sort_transformed_array(nums, a, b, c)
print(sorted_transformed_array)  # [3, 9, 15, 33]