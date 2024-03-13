from typing import List

def min_subarray_len(s: int, nums: List[int]) -> int:
    """
    寻找和至少为s的最小子数组长度。
    
    参数:
    s -- 给定的目标和。
    nums -- 输入的数组。
    
    返回:
    最小子数组的长度，如果不存在则返回0。
    
    示例:
    >>> min_subarray_len(7, [2,3,1,2,4,3])
    2
    """
    # 初始化左右指针和子数组的和
    left = 0
    sum = 0
    min_len = float('inf')  # 用于存储最小长度，初始化为无穷大

    # 遍历数组，移动右指针
    for right in range(len(nums)):
        sum += nums[right]  # 更新子数组的和
        # 当子数组的和至少为s时，尝试收缩窗口
        while sum >= s:
            # 更新最小长度
            min_len = min(min_len, right - left + 1)
            # 移动左指针，减小子数组的和
            sum -= nums[left]
            left += 1
            
    # 检查是否找到了满足条件的子数组
    return min_len if min_len != float('inf') else 0

# 运行示例代码进行测试
print(min_subarray_len(7, [2,3,1,2,4,3]))