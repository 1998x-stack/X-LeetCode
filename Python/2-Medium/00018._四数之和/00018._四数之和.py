from typing import List

def four_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    寻找四数之和为给定目标值的所有不重复四元组。

    Args:
    nums: 整数数组。
    target: 目标和。

    Returns:
    一个包含所有不重复四元组的列表。

    示例:
    >>> four_sum([1, 0, -1, 0, -2, 2], 0)
    [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    """
    nums.sort()  # 对数组进行排序
    n = len(nums)
    result = []

    # 遍历数组，固定前两个数
    for i in range(n - 3):
        # 去重：跳过重复的数字
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            # 去重：跳过重复的数字
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1  # 双指针
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    # 去重：跳过重复的数字
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
    return result

def n_sum(nums: List[int], target: int, n: int) -> List[List[int]]:
    """
    寻找 n 数之和为给定目标值的所有不重复 n 元组。
    
    Args:
    nums: 整数数组。
    target: 目标和。
    n: 元组中数字的数量。
    
    Returns:
    一个包含所有不重复 n 元组的列表。
    """
    def find_n_sum(l: int, r: int, target: int, n: int, result: List[int], results: List[List[int]]):
        if r-l+1 < n or n < 2 or target < nums[l]*n or target > nums[r]*n:  # 剪枝
            return
        if n == 2:  # 两数之和，双指针法
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:  # 递归求解 n-1 数之和
            for i in range(l, r+1):
                if i == l or (i > l and nums[i-1] != nums[i]):
                    find_n_sum(i+1, r, target-nums[i], n-1, result+[nums[i]], results)

    nums.sort()
    results = []
    find_n_sum(0, len(nums)-1, target, n, [], results)
    return results

print(four_sum([1,0,-1,0,-2,2], 0))
# 示例测试
print(n_sum([1, 0, -1, 0, -2, 2], 0, 4))