from typing import List

def count_valid_triangles(nums: List[int]) -> int:
    # 复杂度 O(n^2)
    """
    计算可以组成有效三角形的三元组的数量。
    
    参数:
        nums (List[int]): 给定的整数数组。
        
    返回:
        int: 可以形成的有效三角形的数量。
        
    示例:
        >>> count_valid_triangles([2, 2, 3, 4])
        3
    """
    nums.sort()
    count = 0
    for i in range(len(nums) -2):
        k = i + 2
        for j in range(i+1, len(nums)-1):
            while k < len(nums) and nums[i] + nums[j] > nums[k]:
                k += 1
            count += k - j - 1  # k-1（最后一个满足条件的位置）- j（当前第二个数的位置）
    return count

# 测试代码
nums = [2, 2, 3, 4, 5]
print(f"有效三角形的个数: {count_valid_triangles(nums)}")