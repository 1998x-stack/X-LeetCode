def convert(s: str, numRows: int) -> str:
    """
    实现 Z 字形变换。

    Args:
        s (str): 输入字符串。
        numRows (int): 行数。

    Returns:
        str: 经过 Z 字形变换后的字符串。

    Examples:
        >>> convert("PAYPALISHIRING", 3)
        'PAHNAPLSIIGYIR'
    """
    # 边界条件处理
    if numRows <= 1 or numRows >= len(s):
        return s
    
    # 初始化
    rows = ['' for _ in range(numRows)]  # 每行的字符串
    cur_row = 0  # 当前行
    going_down = False  # 方向标志
    
    # 遍历输入字符串
    for char in s:
        rows[cur_row] += char  # 向当前行添加字符
        # 当在第一行或最后一行时改变方向
        if cur_row == 0 or cur_row == numRows - 1:
            going_down = not going_down
        cur_row += 1 if going_down else -1
    
    # 合并各行字符串
    return ''.join(rows)

# 测试代码
test_output = convert("PAYPALISHIRING", 3)  # 应输出 "PAHNAPLSIIGYIR"
print(test_output)