def convert(s: str, numRows: int) -> str:
    # 处理特殊情况：只有一行或行数超过字符串长度
    if numRows == 1 or numRows >= len(s):
        return s

    # 初始化行字符串列表
    rows = ['' for _ in range(numRows)]
    index, step = 0, 1

    # 遍历字符串，并按照 Z 字形排列
    for char in s:
        rows[index] += char

        # 到达第一行或最后一行时改变方向
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1

        # 更新行索引
        index += step

    # 合并所有行，得到最终字符串
    return ''.join(rows)

# 测试 Z 字形变换函数的正确性和边界情况

def test_convert(func):
    # 测试用例集
    test_cases = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("", 1, ""),
        ("AB", 1, "AB"),
        ("ABCD", 2, "ACBD")
    ]
    
    all_tests_passed = True
    for s, numRows, expected in test_cases:
        result = func(s, numRows)
        if result != expected:
            print(f"测试失败: 输入 '{s}' 和行数 {numRows}，期望 '{expected}'，得到 '{result}'")
            all_tests_passed = False
    
    if all_tests_passed:
        print("所有测试用例都通过了！")

# 测试 convert 函数
test_convert(convert)