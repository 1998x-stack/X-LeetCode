def maximum_swap(num: int) -> int:
    """
    通过一次交换使给定数字尽可能大。
    
    :param num: 给定的非负整数
    :return: 交换后可能的最大整数
    
    详细步骤说明：
    1. 将数字转换成字符数组便于处理。
    2. 使用数组记录每个数字最后出现的位置。
    3. 从左到右扫描，找到第一个可以用更大的数字替换的位置。
    4. 如果找到，执行交换并返回结果。
    """
    # 将数字转换为字符列表
    num_str = list(str(num))
    # 记录每个数字最后出现的位置
    last = {int(x): i for i, x in enumerate(num_str)}
    # 从左到右扫描
    for idx, digit in enumerate(num_str):
        for d in range(9, int(digit), -1):
            if last.get(d, -1) > idx:
                num_str[idx], num_str[last[d]] = num_str[last[d]], num_str[idx]
                return int(''.join(num_str))
    return num
# 测试函数
test_numbers = [2736, 9973, 12345, 54321]
results = [maximum_swap(num) for num in test_numbers]
print(results)