from typing import List
from functools import cmp_to_key

def largestNumber(nums: List[int]) -> str:
    """
    根据给定的非负整数列表，重新排列每个数字以形成最大的数。
    
    参数:
    nums: List[int]: 非负整数列表。
    
    返回:
    str: 重新排列后形成的最大数的字符串表示。
    
    示例:
        输入: [3,30,34,5,9]
        输出: "9534330"
        
    提示:
    - 考虑两个数字的拼接顺序。
    - 注意处理全是0的特殊情况。
    """
    # 将所有数字转换为字符串，便于后续比较
    nums_str = [str(num) for num in nums]
    
    # 自定义排序规则，比较两个字符串拼接的不同顺序的字典序大小
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0
    
    # 根据自定义的比较规则对字符串进行排序
    nums_str.sort(key=cmp_to_key(compare))
    
    # 拼接排序后的字符串
    largest_num = ''.join(nums_str)
    
    # 如果拼接后的字符串首字符为'0'，说明所有数字均为0，直接返回'0'
    return largest_num if largest_num[0] != '0' else '0'

# 测试代码
test_cases = [
    [10, 2],
    [3, 30, 34, 5, 9],
    [0, 0, 0]  # 特殊测试案例，全是0的情况
]

# 执行测试案例
for nums in test_cases:
    print(f"输入: {nums}\n输出: {largestNumber(nums)}\n")