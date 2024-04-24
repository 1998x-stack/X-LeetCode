from typing import List

def isPossible(nums: List[int]) -> bool:
    """ 判断是否可以将数组分割为连续的子序列，每个子序列长度至少为3
    
    Args:
    nums (List[int]): 输入的数字数组
    
    Returns:
    bool: 是否可以分割成满足条件的子序列
    """
    import collections
    count = collections.Counter(nums) # 统计每个数字出现的次数
    end = collections.Counter() # 统计以某个数字结尾的子序列的个数
    for num in nums:
        if count[num] == 0:
            continue
        elif end[num - 1] > 0:
            end[num - 1] -= 1
            end[num] += 1
        elif count[num + 1] > 0 and count[num + 2] > 0:
            count[num + 1] -= 1
            count[num + 2] -= 1
            end[num + 2] += 1
        else:
            return False
        count[num] -= 1
    return True


# 测试代码
nums = [1,2,3,3,4,5]
result = isPossible(nums)
print(f"是否可以分割: {result}")  # 期望输出: True，因为可以分割成 [1,2,3] 和 [3,4,5]