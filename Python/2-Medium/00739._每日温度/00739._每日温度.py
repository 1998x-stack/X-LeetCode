from typing import List

def daily_temperatures(T: List[int]) -> List[int]:
    """
    给定一组温度，找到每一天之后比它温度更高的天数。

    参数:
    T -- 一个整数列表，代表每天的温度。

    返回:
    一个整数列表，表示每一天之后比它温度更高的天数，若不存在则为 0。
    """
    # 初始化一个栈和结果列表，结果长度和输入相同。
    stack = []
    result = [0] * len(T)
    
    # 遍历输入列表
    for curr_day, curr_temp in enumerate(T):
        # 比较栈顶元素和当前元素的温度
        while stack and curr_temp > T[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = curr_day - prev_day
        
        stack.append(curr_day)
    
    return result

# 测试
print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1, 1, 4, 2, 1, 1, 0, 0]
print(daily_temperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))  # [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]