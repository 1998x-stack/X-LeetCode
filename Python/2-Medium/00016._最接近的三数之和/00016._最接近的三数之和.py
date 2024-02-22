def three_sum_closest(nums, target):
    """
    寻找三个数的和，使得这个和最接近给定的目标值。

    参数:
        nums (List[int]): 整数数组。
        target (int): 目标值。

    返回:
        int: 最接近目标值的三个数的和。
    
    示例:
        >>> three_sum_closest([-1, 2, 1, -4], 1)
        2
    """
    nums.sort()  # 对数组进行排序
    closest_sum = float('inf')  # 初始化一个非常大的数表示最接近的和

    for i in range(len(nums) - 2):  # 遍历到倒数第三个数即可
        left, right = i + 1, len(nums) - 1  # 双指针分别指向i之后的第一个数和数组的最后一个数
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]  # 计算当前三个数的和
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum  # 更新最接近的和

            if current_sum < target:  # 如果和小于目标值，则左指针右移
                left += 1
            elif current_sum > target:  # 如果和大于目标值，则右指针左移
                right -= 1
            else:
                return current_sum  # 如果等于目标值，直接返回这个和

    return closest_sum  # 返回最终计算出的最接近的和

# 运行代码
nums = [-1, 2, 1, -4]
target = 1
result = three_sum_closest(nums, target)
print(f"最接近的三数之和为: {result}")