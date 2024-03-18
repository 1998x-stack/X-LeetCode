from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    """
    计算一个数组，使得每个位置的值为除了自身以外其他元素的乘积。

    Args:
    nums: List[int] - 一个整数列表。

    Returns:
    List[int] - 每个位置上除了自身以外其他元素的乘积列表。

    示例：
    输入: [1,2,3,4]
    输出: [24,12,8,6]
    """
    n = len(nums)
    left_products = [1] * n  # 初始化左乘积数组
    right_products = [1] * n  # 初始化右乘积数组
    answer = [0] * n  # 初始化答案数组

    # 填充左乘积数组
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    # 填充右乘积数组
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    # 计算结果
    for i in range(n):
        answer[i] = left_products[i] * right_products[i]

    return answer

# 测试代码
nums = [1, 2, 3, 4]
print(product_except_self(nums))