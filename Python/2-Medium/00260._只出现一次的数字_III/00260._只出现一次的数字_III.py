from typing import List

def find_single_numbers(nums: List[int]) -> List[int]:
    """
    在给定的数组中找到只出现一次的两个数字。

    Args:
    nums: List[int] - 一个整数数组，其中有两个元素只出现一次，其他元素均出现两次。

    Returns:
    List[int] - 只出现一次的两个数字。
    
    示例:
    >>> find_single_numbers([1,2,1,3,2,5])
    [3,5]
    """
    # 整体异或得到两个只出现一次的数字的异或结果
    xor_result = 0
    for num in nums:
        xor_result ^= num
    
    # 找到异或结果中任意一个为 1 的位
    # 这里用到了位运算技巧：x & (-x) 可以得到 x 的二进制表示中最低位的 1
    right_most_bit = xor_result & (-xor_result)
    
    # 根据该位将原数组分为两组，并分别进行异或操作
    num1, num2 = 0, 0
    for num in nums:
        # 如果该位为 1
        if num & right_most_bit:
            num1 ^= num
        else:
            num2 ^= num
    
    return [num1, num2]

# 运行代码并打印结果
print(find_single_numbers([1,2,1,3,2,5]))