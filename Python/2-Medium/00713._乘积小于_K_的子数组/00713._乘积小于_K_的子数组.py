from typing import List

def count_subarrays_with_product_less_than_k(nums: List[int], k: int) -> int:
    """
    计算乘积小于 k 的子数组个数

    参数:
    nums (List[int]): 正整数数组
    k (int): 乘积阈值

    返回:
    int: 乘积小于 k 的子数组数量

    示例:
    >>> count_subarrays_with_product_less_than_k([10, 5, 2, 6], 100)
    8
    """
    start = 0
    count = 0
    current_product = 1
    for end in range(len(nums)):
        current_product *= nums[end]
        while current_product >= k and start <= end:
            current_product /= nums[start]
            start += 1
        
        count += end - start + 1
    return count

if __name__ == "__main__":
    # 测试算法的正确性
    test_nums = [10, 5, 2, 6]
    test_k = 100
    result = count_subarrays_with_product_less_than_k(test_nums, test_k)
    print(result)